/* MBT admin — galeria z drag & drop:
   - przeciąganie miniaturek zmienia kolejność (aktualizuje JSON w textarea)
   - nowe pliki dostają placeholder __new_N__ (po zapisie zamieniany na URL)
   - przycisk × usuwa zdjęcie
*/
(function () {
  'use strict';

  var newCounter = 0;

  function updateCount(wrap) {
    var thumbs = wrap.querySelectorAll('.mbt-gallery-thumb-wrap');
    var countEl = wrap.querySelector('.mbt-gallery-count');
    if (countEl) {
      var n = thumbs.length;
      countEl.textContent = n + (n === 1 ? ' zdjęcie' : (n % 10 >= 2 && n % 10 <= 4 && (n % 100 < 12 || n % 100 > 14) ? ' zdjęcia' : ' zdjęć'));
    }
  }

  function showProgress(wrap, loaded, total) {
    var bar = wrap.querySelector('.mbt-upload-progress');
    if (!bar) return;
    bar.hidden = false;
    var pct = total ? Math.min(100, Math.round(loaded / total * 100)) : 0;
    var inner = bar.querySelector('.mbt-upload-progress-bar');
    if (inner) inner.style.width = pct + '%';
    var txt = bar.querySelector('.mbt-upload-progress-text');
    if (txt) txt.textContent = 'Przygotowywanie zdjęć… ' + pct + '%';
  }

  function hideProgress(wrap) {
    var bar = wrap.querySelector('.mbt-upload-progress');
    if (bar) bar.hidden = true;
    var done = wrap.querySelector('.mbt-upload-done');
    if (done) done.hidden = false;
  }

  function syncJson(wrap) {
    var thumbs = wrap.querySelector('.mbt-gallery-thumbs');
    var json = wrap.querySelector('.mbt-gallery-json');
    if (!thumbs || !json) return;
    var urls = [];
    thumbs.querySelectorAll('.mbt-gallery-thumb-wrap').forEach(function (t) {
      if (t.dataset.url) {
        urls.push(t.dataset.url);
      } else if (t.dataset.new !== undefined) {
        urls.push('__new_' + t.dataset.new + '__');
      }
    });
    json.value = JSON.stringify(urls);
  }

  function addThumb(wrap, src, data) {
    var thumbs = wrap.querySelector('.mbt-gallery-thumbs');
    var empty = wrap.querySelector('.mbt-upload-empty');
    if (empty) empty.remove();
    var t = document.createElement('div');
    t.className = 'mbt-gallery-thumb-wrap';
    t.draggable = true;
    if (data.url) t.dataset.url = data.url;
    if (data.new !== undefined) t.dataset.new = data.new;
    var img = document.createElement('img');
    img.src = src;
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

  function previewFiles(input) {
    var files = Array.prototype.slice.call(input.files || []);
    if (!files.length) return;
    var wrap = input.closest('.mbt-upload, .mbt-gallery');

    if (input.dataset.preview === '1') {
      // pojedyncze zdjęcie/wideo: pokaż podgląd nowego pliku
      var img = wrap.querySelector('.mbt-upload-img');
      var video = wrap.querySelector('.mbt-upload-video');
      var empty = wrap.querySelector('.mbt-upload-empty');
      var done = wrap.querySelector('.mbt-upload-done');
      var reader = new FileReader();
      reader.onload = function (e) {
        if (video) {
          video.src = e.target.result;
          video.controls = true;
          video.style.display = '';
        } else if (img) {
          img.src = e.target.result;
          img.style.display = '';
        }
        if (empty) { empty.style.display = 'none'; }
        if (done) { done.hidden = false; }
      };
      reader.readAsDataURL(files[0]);
    }

    if (input.dataset.gallery === '1') {
      // galeria: podgląd miniatur + placeholder w JSON (kolejność = drag&drop)
      // UWAGA: NIE czyścimy inputa (value='') — pliki muszą zostać w inputcie,
      // żeby przy zapisie formularza poleciały na serwer (value_from_datadict).
      var total = 0, loaded = 0;
      files.forEach(function (f) { total += f.size || 0; });
      files.forEach(function (f) {
        var idx = newCounter++;
        var reader = new FileReader();
        reader.onprogress = function (e) {
          if (e.lengthComputable) {
            loaded += e.loaded;
            showProgress(wrap, loaded, total);
          }
        };
        reader.onload = (function (i) {
          return function (e) {
            addThumb(wrap, e.target.result, { new: i });
            syncJson(wrap);
            updateCount(wrap);
            if (--pending === 0) hideProgress(wrap);
          };
        })(idx);
        reader.readAsDataURL(f);
      });
      var pending = files.length;
      showProgress(wrap, 0, total);
    }
  }

  /* --- drag & drop sortowanie --- */
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
    var wrap = e.target.closest('.mbt-gallery');
    syncJson(wrap);
    updateCount(wrap);
  });

  document.addEventListener('dragend', function () {
    if (dragEl) {
      dragEl.classList.remove('mbt-dragging');
      dragEl = null;
    }
  });

  /* --- usuwanie zdjęcia --- */
  document.addEventListener('click', function (e) {
    var btn = e.target.closest('.mbt-gallery-remove');
    if (!btn) return;
    var wrap = btn.closest('.mbt-gallery');
    var t = btn.closest('.mbt-gallery-thumb-wrap');
    if (t) t.remove();
    if (wrap) { syncJson(wrap); updateCount(wrap); }
  });

  /* --- licznik przy starcie --- */
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.mbt-gallery').forEach(function (wrap) {
      updateCount(wrap);
    });
  });

  /* --- Kompresja obrazu po stronie przeglądarki (Canvas) --- */
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

        // Wypełnij tło na biało w przypadku przezroczystości (konwersja na JPEG)
        ctx.fillStyle = '#FFFFFF';
        ctx.fillRect(0, 0, w, h);
        ctx.drawImage(img, 0, 0, w, h);

        var outType = 'image/jpeg';
        canvas.toBlob(function (blob) {
          if (!blob) {
            return callback(file);
          }
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

  /* --- Cropper helper --- */
  function openCropper(file, aspectRatio, onCrop, onCancel) {
    var overlay = document.createElement('div');
    overlay.style.position = 'fixed';
    overlay.style.top = '0';
    overlay.style.left = '0';
    overlay.style.width = '100%';
    overlay.style.height = '100%';
    overlay.style.backgroundColor = 'rgba(0,0,0,0.8)';
    overlay.style.zIndex = '999999';
    overlay.style.display = 'flex';
    overlay.style.flexDirection = 'column';
    overlay.style.alignItems = 'center';
    overlay.style.justifyContent = 'center';

    var imgWrap = document.createElement('div');
    imgWrap.style.width = '80%';
    imgWrap.style.height = '80%';
    imgWrap.style.backgroundColor = '#222';
    imgWrap.style.marginBottom = '20px';
    var img = document.createElement('img');
    img.style.maxWidth = '100%';
    img.style.maxHeight = '100%';
    imgWrap.appendChild(img);
    
    var btnWrap = document.createElement('div');
    var btnSave = document.createElement('button');
    btnSave.textContent = 'Zapisz (Przytnij)';
    btnSave.className = 'button default';
    btnSave.style.padding = '10px 20px';
    btnSave.style.marginRight = '10px';
    btnSave.style.cursor = 'pointer';
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
    reader.onload = function(e) {
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
      if (overlay.parentNode) {
        document.body.removeChild(overlay);
      }
    }

    btnCancel.addEventListener('click', function() {
      close();
      if (onCancel) onCancel();
    });

    btnSave.addEventListener('click', function() {
      if (!cropper) return;
      var baseName = (file.name || 'image').replace(/\.[^/.]+$/, '');
      cropper.getCroppedCanvas({
        maxWidth: 1600,
        maxHeight: 1600,
      }).toBlob(function(blob) {
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
      }, 'image/jpeg', 0.85);
    });
  }

  /* --- zmiana pliku (nowe zdjęcia) --- */
  document.addEventListener('change', function (e) {
    if (e.target && e.target.classList.contains('mbt-upload-file')) {
      var input = e.target;
      var files = input.files;
      if (!files || !files.length) return;

      var isCrop = input.getAttribute('data-crop') === '1';
      var aspectRatio = input.getAttribute('data-aspect-ratio');
      var isVideo = files[0].type.indexOf('video') === 0;

      if (input.dataset.gallery === '1') {
        // Multi-upload galeria: automatyczna kompresja każdego zdjęcia
        var fileList = Array.prototype.slice.call(files);
        var compressedList = [];
        var total = fileList.length;
        var processed = 0;

        fileList.forEach(function (f, idx) {
          compressImage(f, 1920, 0.85, function (compFile) {
            compressedList[idx] = compFile;
            processed++;
            if (processed === total) {
              var dt = new DataTransfer();
              compressedList.forEach(function (cf) { dt.items.add(cf); });
              input.files = dt.files;
              previewFiles(input);
            }
          });
        });
      } else if (isCrop && typeof Cropper !== 'undefined' && !isVideo) {
        // Przed otwarciem croppera zoptymalizuj ewentualne ogromne pliki z aparatu
        compressImage(files[0], 2400, 0.9, function (optFile) {
          openCropper(optFile, aspectRatio, function (croppedFile) {
            var dt = new DataTransfer();
            dt.items.add(croppedFile);
            input.files = dt.files;
            previewFiles(input);
          }, function () {
            input.value = '';
          });
        });
      } else if (!isVideo) {
        // Pojedyncze zdjęcie bez croppera: automatyczna kompresja do 1920px JPEG
        compressImage(files[0], 1920, 0.85, function (compressedFile) {
          var dt = new DataTransfer();
          dt.items.add(compressedFile);
          input.files = dt.files;
          previewFiles(input);
        });
      } else {
        // Wideo
        previewFiles(input);
      }
    }
  });

  /* --- Zabezpieczenie przed limitem Vercel (4.5 MB) przy wysyłce formularza --- */
  document.addEventListener('submit', function (e) {
    var form = e.target;
    if (!form || !form.querySelectorAll) return;
    var fileInputs = form.querySelectorAll('input[type="file"]');
    var totalBytes = 0;
    fileInputs.forEach(function (inp) {
      if (inp.files) {
        for (var i = 0; i < inp.files.length; i++) {
          totalBytes += inp.files[i].size || 0;
        }
      }
    });
    // 4.2 MB limit ostrzegawczy (Vercel payload limit to 4.5 MB)
    if (totalBytes > 4.2 * 1024 * 1024) {
      e.preventDefault();
      alert('Rozmiar wybranych plików (' + (totalBytes / (1024 * 1024)).toFixed(1) + ' MB) przekracza dopuszczalny limit 4.5 MB na serwerze Vercel.\n\nProsimy o wybranie mniejszych plików lub zmniejszenie ich przed zapisem.');
      return false;
    }
  });
})();
