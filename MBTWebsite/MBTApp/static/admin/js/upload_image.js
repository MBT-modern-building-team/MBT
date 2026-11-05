/* MBT Admin — Asynchroniczny Upload na Cloudflare R2 + Galeria z Drag & Drop:
   - Zdjęcia są wgrywane pojedynczo przez AJAX (/admin/api/upload-r2/) bezpośrednio na R2
   - Baner statusu pokazuje postęp i informuje, kiedy MOŻNA kliknąć „Zapisz"
   - Przyciski zapisu są blokowane podczas trwania uploadu (zabezpieczenie przed błędem 500)
   - Inputy type="file" są czyszczone po uploadzie — formularz wysyła wyłącznie lekkie URL-e
   - Obsługa kadrowania (Cropper.js) i sortowania miniatur (drag & drop)
*/
(function () {
  'use strict';

  var activeUploads = 0;

  /* --- Pobieranie tokenu CSRF --- */
  function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }

  function getCsrfToken() {
    var csrfInput = document.querySelector('input[name="csrfmiddlewaretoken"]');
    if (csrfInput && csrfInput.value) return csrfInput.value;
    return getCookie('csrftoken') || '';
  }

  /* --- Zarządzanie blokadą przycisków zapisu (Save) --- */
  function updateSubmitLock() {
    var submitButtons = document.querySelectorAll(
      '.submit-row input[type="submit"], .submit-row button[type="submit"], input[type="submit"].default, form input[type="submit"]'
    );
    var submitRows = document.querySelectorAll('.submit-row');

    submitRows.forEach(function (row) {
      var notice = row.querySelector('.mbt-submit-lock-notice');
      if (activeUploads > 0) {
        if (!notice) {
          notice = document.createElement('div');
          notice.className = 'mbt-submit-lock-notice';
          row.insertBefore(notice, row.firstChild);
        }
        notice.textContent = '⏳ Trwa przesyłanie zdjęć na Cloudflare R2... Przycisk Zapisz jest zablokowany do zakończenia wgrywania.';
      } else {
        if (notice) notice.remove();
      }
    });

    submitButtons.forEach(function (btn) {
      if (activeUploads > 0) {
        btn.disabled = true;
        if (!btn.dataset.origTitle) btn.dataset.origTitle = btn.title || '';
        btn.title = 'Trwa wgrywanie zdjęć na Cloudflare R2... Poczekaj przed kliknięciem Zapisz';
      } else {
        btn.disabled = false;
        btn.title = btn.dataset.origTitle || '';
      }
    });
  }

  function startUpload() {
    activeUploads++;
    updateSubmitLock();
  }

  function finishUpload() {
    activeUploads = Math.max(0, activeUploads - 1);
    updateSubmitLock();
  }

  /* --- Kontroler Banera Statusu R2 --- */
  function setBannerStatus(wrap, status, title, detail, progressPct) {
    var banner = wrap.querySelector('.mbt-r2-banner');
    if (!banner) return;

    if (status === 'idle') {
      banner.style.display = 'none';
      banner.dataset.r2Status = 'idle';
      return;
    }

    banner.style.display = 'flex';
    banner.dataset.r2Status = status; // 'uploading' | 'success' | 'error'

    var titleEl = banner.querySelector('.mbt-r2-banner-title');
    if (titleEl) titleEl.textContent = title || '';

    var detailEl = banner.querySelector('.mbt-r2-banner-detail');
    if (detailEl) detailEl.textContent = detail || '';

    var progressWrap = banner.querySelector('.mbt-r2-progress-wrap');
    var progressBar = banner.querySelector('.mbt-r2-progress-bar');
    if (progressWrap && progressBar) {
      if (typeof progressPct === 'number' && progressPct >= 0) {
        progressWrap.style.display = 'block';
        progressBar.style.width = Math.min(100, Math.round(progressPct)) + '%';
      } else {
        progressWrap.style.display = 'none';
      }
    }
  }

  /* --- Wysyłanie pliku przez AJAX na Cloudflare R2 (bezpośrednio lub przez serwer) --- */
  function uploadFileToR2(file, folder, onProgress, onSuccess, onError) {
    var isVideo = file.type && file.type.indexOf('video') === 0;
    var isLarge = file.size > 3.5 * 1024 * 1024;

    // Duże pliki (> 3.5 MB) lub wideo wgrywamy BEZPOŚREDNIO na Cloudflare R2 przez Presigned URL.
    // Dzięki temu omijamy twardy limit Vercela (4.5 MB), który powodował błąd serwera (kod 413).
    if (isVideo || isLarge) {
      var pReq = new XMLHttpRequest();
      pReq.open('POST', '/admin/api/upload-r2/', true);
      pReq.setRequestHeader('X-CSRFToken', getCsrfToken());

      var pData = new FormData();
      pData.append('action', 'get_presigned_url');
      pData.append('filename', file.name || (isVideo ? 'video.mp4' : 'file.bin'));
      pData.append('folder', folder || 'uploads');
      pData.append('content_type', file.type || (isVideo ? 'video/mp4' : 'application/octet-stream'));

      pReq.onload = function () {
        var pDataResp = null;
        try { pDataResp = JSON.parse(pReq.responseText); } catch (e) {}

        if (pReq.status >= 200 && pReq.status < 300 && pDataResp && pDataResp.success && pDataResp.upload_url) {
          // Bezpośredni upload z przeglądarki na Cloudflare R2 (brak ograniczenia rozmiaru Vercela)
          var r2Xhr = new XMLHttpRequest();
          r2Xhr.open('PUT', pDataResp.upload_url, true);
          if (pDataResp.content_type) {
            r2Xhr.setRequestHeader('Content-Type', pDataResp.content_type);
          }

          if (r2Xhr.upload && onProgress) {
            r2Xhr.upload.onprogress = function (e) {
              if (e.lengthComputable) {
                var pct = (e.loaded / e.total) * 100;
                onProgress(pct);
              }
            };
          }

          r2Xhr.onload = function () {
            if (r2Xhr.status >= 200 && r2Xhr.status < 300) {
              onSuccess(pDataResp.public_url, pDataResp);
            } else {
              onError('Błąd bezpośredniego wgrywania na Cloudflare R2 (kod ' + r2Xhr.status + ').');
            }
          };

          r2Xhr.onerror = function () {
            onError('Błąd połączenia sieciowego podczas wgrywania na Cloudflare R2.');
          };

          r2Xhr.send(file);
        } else {
          var err = (pDataResp && pDataResp.error) ? pDataResp.error : ('Błąd inicjalizacji R2 (kod ' + pReq.status + ')');
          onError(err);
        }
      };

      pReq.onerror = function () {
        onError('Błąd połączenia z serwerem podczas przygotowywania uploadu.');
      };

      pReq.send(pData);
      return;
    }

    // Dla małych plików (np. skadrowane zdjęcia < 3.5 MB) — standardowy upload przez Django
    var formData = new FormData();
    formData.append('file', file);
    if (folder) formData.append('folder', folder);

    var xhr = new XMLHttpRequest();
    xhr.open('POST', '/admin/api/upload-r2/', true);
    xhr.setRequestHeader('X-CSRFToken', getCsrfToken());

    if (xhr.upload && onProgress) {
      xhr.upload.onprogress = function (e) {
        if (e.lengthComputable) {
          var pct = (e.loaded / e.total) * 100;
          onProgress(pct);
        }
      };
    }

    xhr.onload = function () {
      var data = null;
      try {
        data = JSON.parse(xhr.responseText);
      } catch (err) {
        data = null;
      }

      if (xhr.status >= 200 && xhr.status < 300 && data && data.success) {
        onSuccess(data.url, data);
      } else {
        var errMsg = (data && data.error) ? data.error : ('Błąd serwera (kod ' + xhr.status + ')');
        onError(errMsg);
      }
    };

    xhr.onerror = function () {
      onError('Błąd połączenia sieciowego podczas wysyłania pliku na serwer.');
    };

    xhr.send(formData);
  }

  /* --- Galeria: funkcje pomocnicze miniatur i JSON --- */
  function updateCount(wrap) {
    var thumbs = wrap.querySelectorAll('.mbt-gallery-thumb-wrap');
    var countEl = wrap.querySelector('.mbt-gallery-count');
    if (countEl) {
      var n = thumbs.length;
      countEl.textContent = n + (n === 1 ? ' zdjęcie' : (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 12 || n % 100 > 14) ? ' zdjęcia' : ' zdjęć'));
    }
  }

  function syncJson(wrap) {
    var thumbs = wrap.querySelector('.mbt-gallery-thumbs');
    var json = wrap.querySelector('.mbt-gallery-json');
    if (!thumbs || !json) return;
    var urls = [];
    thumbs.querySelectorAll('.mbt-gallery-thumb-wrap').forEach(function (t) {
      if (t.dataset.url) {
        urls.push(t.dataset.url);
      }
    });
    json.value = JSON.stringify(urls);
  }

  function addThumb(wrap, url) {
    var thumbs = wrap.querySelector('.mbt-gallery-thumbs');
    var empty = wrap.querySelector('.mbt-upload-empty');
    if (empty) empty.remove();

    var t = document.createElement('div');
    t.className = 'mbt-gallery-thumb-wrap';
    t.draggable = true;
    t.dataset.url = url;

    var img = document.createElement('img');
    img.src = url;
    img.className = 'mbt-gallery-thumb';
    img.alt = '';

    var handle = document.createElement('span');
    handle.className = 'mbt-gallery-drag-handle';
    handle.textContent = '⠿';

    var btn = document.createElement('button');
    btn.type = 'button';
    btn.className = 'mbt-gallery-remove';
    btn.title = 'Usuń zdjęcie';
    btn.textContent = '×';

    t.appendChild(img);
    t.appendChild(handle);
    t.appendChild(btn);
    thumbs.appendChild(t);
    return t;
  }

  /* --- Drag & Drop w Galerii --- */
  var dragEl = null;

  document.addEventListener('dragstart', function (e) {
    var t = e.target.closest('.mbt-gallery-thumb-wrap');
    if (!t) return;
    dragEl = t;
    t.classList.add('mbt-dragging');
    e.dataTransfer.effectAllowed = 'move';
    e.dataTransfer.setData('text/plain', '');
  });

  document.addEventListener('dragover', function (e) {
    var t = e.target.closest('.mbt-gallery-thumbs');
    if (!t || !dragEl) return;
    e.preventDefault();
    e.dataTransfer.dropEffect = 'move';
  });

  document.addEventListener('drop', function (e) {
    var wrap = e.target.closest('.mbt-gallery-thumbs');
    if (!wrap || !dragEl) return;
    e.preventDefault();
    var target = e.target.closest('.mbt-gallery-thumb-wrap');
    if (target && target !== dragEl) {
      var rect = target.getBoundingClientRect();
      var after = e.clientX > rect.left + rect.width / 2;
      if (after) {
        target.after(dragEl);
      } else {
        target.before(dragEl);
      }
    } else if (!target) {
      wrap.appendChild(dragEl);
    }
    dragEl.classList.remove('mbt-dragging');
    dragEl = null;
    var galleryWrap = wrap.closest('.mbt-gallery');
    syncJson(galleryWrap);
    updateCount(galleryWrap);
  });

  document.addEventListener('dragend', function () {
    if (dragEl) {
      dragEl.classList.remove('mbt-dragging');
      dragEl = null;
    }
  });

  /* --- Usuwanie zdjęcia z galerii --- */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.mbt-gallery-remove');
    if (!btn) return;
    var galleryWrap = btn.closest('.mbt-gallery');
    var t = btn.closest('.mbt-gallery-thumb-wrap');
    if (t) t.remove();
    if (galleryWrap) {
      syncJson(galleryWrap);
      updateCount(galleryWrap);
    }
  });

  /* --- Kompresja po stronie przeglądarki przed wysłaniem (Canvas) --- */
  function compressImage(file, maxDim, quality, callback) {
    if (!file || !file.type || !file.type.startsWith('image/') || file.type === 'image/svg+xml') {
      return callback(file);
    }

    var reader = new FileReader();
    reader.onload = function (e) {
      var img = new Image();
      img.onload = function () {
        var w = img.width;
        var h = img.height;
        var max = maxDim || 1920;
        if (w > max || h > max) {
          if (w > h) {
            h = Math.round(h * (max / w));
            w = max;
          } else {
            w = Math.round(w * (max / h));
            h = max;
          }
        }
        var canvas = document.createElement('canvas');
        canvas.width = w;
        canvas.height = h;
        var ctx = canvas.getContext('2d');

        // Wypełnij tło na biało w przypadku przezroczystości
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(0, 0, w, h);
        ctx.drawImage(img, 0, 0, w, h);

        var outType = 'image/jpeg';
        canvas.toBlob(function (blob) {
          if (!blob) return callback(file);
          var baseName = (file.name || 'image').replace(/\.[^/.]+$/, '');
          var compressedFile = new File([blob], baseName + '.jpg', {
            type: outType,
            lastModified: Date.now()
          });
          callback(compressedFile);
        }, outType, quality || 0.85);
      };
      img.onerror = function () {
        callback(file);
      };
      img.src = e.target.result;
    };
    reader.onerror = function () {
      callback(file);
    };
    reader.readAsDataURL(file);
  }

  /* --- Cropper modal --- */
  function openCropper(file, aspectRatio, onCrop, onCancel) {
    var overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0,0,0,0.85)';
    overlay.style.zIndex = '999999';
    overlay.style.display = 'flex';
    overlay.style.flexDirection = 'column';
    overlay.style.alignItems = 'center';
    overlay.style.justifyContent = 'center';

    var imgWrap = document.createElement('div');
    imgWrap.style.width = '80%';
    imgWrap.style.height = '75%';
    imgWrap.style.backgroundColor = '#1e293b';
    imgWrap.style.marginBottom = '20px';
    imgWrap.style.borderRadius = '8px';
    imgWrap.style.overflow = 'hidden';

    var img = document.createElement('img');
    img.style.maxWidth = '100%';
    img.style.maxHeight = '100%';
    imgWrap.appendChild(img);

    var btnWrap = document.createElement('div');
    var btnSave = document.createElement('button');
    btnSave.textContent = 'Zapisz i wgraj na R2';
    btnSave.className = 'button default';
    btnSave.style.padding = '10px 24px';
    btnSave.style.marginRight = '12px';
    btnSave.style.cursor = 'pointer';
    btnSave.style.fontWeight = 'bold';
    btnSave.type = 'button';

    var btnCancel = document.createElement('button');
    btnCancel.textContent = 'Anuluj';
    btnCancel.className = 'button';
    btnCancel.style.padding = '10px 20px';
    btnCancel.style.cursor = 'pointer';
    btnCancel.type = 'button';

    btnWrap.appendChild(btnSave);
    btnWrap.appendChild(btnCancel);
    overlay.appendChild(imgWrap);
    overlay.appendChild(btnWrap);
    document.body.appendChild(overlay);

    var cropper = null;
    var reader = new FileReader();
    reader.onload = function (e) {
      img.src = e.target.result;
      var cropperOptions = {
        viewMode: 1,
        autoCropArea: 1,
      };
      if (aspectRatio) {
        cropperOptions.aspectRatio = parseFloat(aspectRatio);
      }
      cropper = new Cropper(img, cropperOptions);
    };
    reader.readAsDataURL(file);

    function close() {
      if (cropper) cropper.destroy();
      if (overlay.parentNode) document.body.removeChild(overlay);
    }

    btnCancel.addEventListener('click', function () {
      close();
      if (onCancel) onCancel();
    });

    btnSave.addEventListener('click', function () {
      if (!cropper) return;
      var baseName = (file.name || 'image').replace(/\.[^/.]+$/, '');
      cropper.getCroppedCanvas({
        maxWidth: 1920,
        maxHeight: 1920,
      }).toBlob(function (blob) {
        if (!blob) {
          close();
          return;
        }
        var croppedFile = new File([blob], baseName + '.jpg', {
          type: 'image/jpeg',
          lastModified: Date.now()
        });
        close();
        onCrop(croppedFile);
      }, 'image/jpeg', 0.88);
    });
  }

  /* --- Obsługa wyboru pojedynczego pliku (zdjęcie / wideo) --- */
  function handleSingleUpload(input, file) {
    var wrap = input.closest('.mbt-upload');
    if (!wrap) return;

    var isVideo = file.type.indexOf('video') === 0;
    var urlInput = wrap.querySelector('[data-url-input="1"]');
    var imgEl = wrap.querySelector('.mbt-upload-img');
    var videoEl = wrap.querySelector('.mbt-upload-video');
    var emptyEl = wrap.querySelector('.mbt-upload-empty');

    startUpload();
    setBannerStatus(
      wrap,
      'uploading',
      'Trwa przesyłanie na Cloudflare R2... Proszę czekać, NIE klikaj jeszcze Zapisz.',
      file.name + ' (' + (file.size / 1024).toFixed(0) + ' KB)',
      10
    );

    uploadFileToR2(
      file,
      'uploads',
      function (pct) {
        setBannerStatus(
          wrap,
          'uploading',
          'Trwa przesyłanie na Cloudflare R2 (' + Math.round(pct) + '%)... Proszę czekać, NIE klikaj jeszcze Zapisz.',
          file.name + ' (' + (file.size / 1024).toFixed(0) + ' KB)',
          pct
        );
      },
      function (url) {
        // Sukces
        if (urlInput) {
          urlInput.value = url;
          urlInput.dispatchEvent(new Event('change', { bubbles: true }));
        }
        if (isVideo && videoEl) {
          videoEl.src = url;
          videoEl.controls = true;
          videoEl.style.display = '';
          if (emptyEl) emptyEl.style.display = 'none';
        } else if (imgEl) {
          imgEl.src = url;
          imgEl.style.display = '';
          if (emptyEl) emptyEl.style.display = 'none';
        }

        // Czyścimy plik z inputa — formularz zapisze lekki URL z urlInput!
        input.value = '';

        setBannerStatus(
          wrap,
          'success',
          isVideo ? '✓ Film został wgrany na Cloudflare R2! MOŻESZ TERAZ ZAPISAĆ ZMIANY.' : '✓ Zdjęcie zostało wgrane na Cloudflare R2! MOŻESZ TERAZ ZAPISAĆ ZMIANY.',
          url,
          100
        );
        finishUpload();
      },
      function (errMsg) {
        // Błąd
        input.value = '';
        setBannerStatus(
          wrap,
          'error',
          '❌ Błąd podczas wgrywania na Cloudflare R2',
          errMsg,
          0
        );
        finishUpload();
      }
    );
  }

  /* --- Obsługa wyboru wielu zdjęć w galerii --- */
  function handleGalleryUpload(input, rawFiles) {
    var wrap = input.closest('.mbt-gallery');
    if (!wrap) return;

    var files = Array.prototype.slice.call(rawFiles || []);
    if (!files.length) return;

    var totalFiles = files.length;
    var currentIndex = 0;
    var successCount = 0;

    startUpload();
    setBannerStatus(
      wrap,
      'uploading',
      'Wgrywanie na Cloudflare R2: plik 1 z ' + totalFiles + '... Proszę czekać, NIE klikaj jeszcze Zapisz.',
      files[0].name,
      5
    );

    function uploadNext() {
      if (currentIndex >= totalFiles) {
        // Koniec całej kolejki galerii
        input.value = '';
        setBannerStatus(
          wrap,
          'success',
          '✓ Wszystkie zdjęcia (' + successCount + ') zostały pomyślnie wgrane na Cloudflare R2! MOŻESZ TERAZ ZAPISAĆ ZMIANY.',
          'Wszystkie miniatury zostały zaktualizowane o docelowe linki media.mbt.pl.',
          100
        );
        finishUpload();
        return;
      }

      var currentFile = files[currentIndex];
      var fileNum = currentIndex + 1;
      var baseProgress = ((fileNum - 1) / totalFiles) * 100;

      setBannerStatus(
        wrap,
        'uploading',
        'Wgrywanie na Cloudflare R2: plik ' + fileNum + ' z ' + totalFiles + ' (' + Math.round(baseProgress) + '%)... Proszę czekać, NIE klikaj jeszcze Zapisz.',
        currentFile.name + ' (' + (currentFile.size / 1024).toFixed(0) + ' KB)',
        baseProgress
      );

      // Najpierw kompresja Canvas (max 1920px), a potem wysyłka na R2
      compressImage(currentFile, 1920, 0.85, function (compFile) {
        uploadFileToR2(
          compFile,
          'uploads',
          function (filePct) {
            var totalPct = baseProgress + (filePct / totalFiles);
            setBannerStatus(
              wrap,
              'uploading',
              'Wgrywanie na Cloudflare R2: plik ' + fileNum + ' z ' + totalFiles + ' (' + Math.round(totalPct) + '%)... Proszę czekać, NIE klikaj jeszcze Zapisz.',
              currentFile.name,
              totalPct
            );
          },
          function (url) {
            // Dodaj miniaturę od razu po wgraniu pliku
            addThumb(wrap, url);
            syncJson(wrap);
            updateCount(wrap);
            successCount++;

            currentIndex++;
            uploadNext();
          },
          function (errMsg) {
            input.value = '';
            setBannerStatus(
              wrap,
              'error',
              '❌ Błąd wgrywania pliku ' + currentFile.name + ' na Cloudflare R2',
              errMsg + ' (Wgrano pomyślnie ' + successCount + ' z ' + totalFiles + ' zdjęć).',
              0
            );
            finishUpload();
          }
        );
      });
    }

    uploadNext();
  }

  /* --- Nasłuchiwanie zmian w polach plików --- */
  document.addEventListener('change', function (e) {
    if (e.target && e.target.classList.contains('mbt-upload-file')) {
      var input = e.target;
      var files = input.files;
      if (!files || !files.length) return;

      var isCrop = input.getAttribute('data-crop') === '1';
      var aspectRatio = input.getAttribute('data-aspect-ratio');
      var isVideo = files[0].type.indexOf('video') === 0;

      if (input.dataset.gallery === '1') {
        // Multi-upload galeria
        handleGalleryUpload(input, files);
      } else if (isCrop && typeof Cropper !== 'undefined' && !isVideo) {
        // Pojedyncze zdjęcie z Cropperem
        compressImage(files[0], 2400, 0.9, function (optFile) {
          openCropper(
            optFile,
            aspectRatio,
            function (croppedFile) {
              handleSingleUpload(input, croppedFile);
            },
            function () {
              input.value = '';
            }
          );
        });
      } else if (!isVideo) {
        // Pojedyncze zdjęcie bez croppera — kompresja i wysyłka
        compressImage(files[0], 1920, 0.85, function (compFile) {
          handleSingleUpload(input, compFile);
        });
      } else {
        // Wideo
        handleSingleUpload(input, files[0]);
      }
    }
  });

  /* --- Zabezpieczenie przed przedwczesnym wysłaniem formularza --- */
  document.addEventListener('submit', function (e) {
    if (activeUploads > 0) {
      e.preventDefault();
      alert('⚠️ Trwa przesyłanie zdjęć na Cloudflare R2!\n\nProszę poczekać na zakończenie wgrywania (zielony baner) przed zapisaniem formularza.');
      return false;
    }
  });

  /* --- Inicjalizacja przy załadowaniu DOM --- */
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.mbt-gallery').forEach(function (wrap) {
      updateCount(wrap);
    });
  });
})();
