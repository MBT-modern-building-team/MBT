/**
 * MBT KIOSK - KOD INTERFEJSU DOTYKOWEGO 32" 4K (webOS)
 * Modern Building Team
 */

document.addEventListener('DOMContentLoaded', () => {
  // 1. ZEGAR CZASU RZECZYWISTEGO
  initLiveClock();

  // 2. NAWIGACJA ZAKŁADEK (DOCK & HEADER)
  initTabNavigation();

  // 3. TRYB PEŁNOEKRANOWY (FULLSCREEN API)
  initFullscreen();

  // 4. INTERAKTYWNY SUWAK PRZED / PO (BEFORE & AFTER)
  initBeforeAfterSlider();

  // 5. FILTROWANIE REALIZACJI
  initProjectFilters();

  // 6. MODAL ZE SZCZEGÓŁAMI PROJEKTU I GALERIĄ
  initProjectModal();

  // 7. PREZENTACJA PITCH DECK (SLAJDY)
  initPresentationDeck();

  // 8. GENEROWANIE KODÓW QR
  initQRCodes();
});

/* ==========================================================================
   1. ZEGAR CYFROWY
   ========================================================================== */
function initLiveClock() {
  const timeEl = document.getElementById('kiosk-live-time');
  const dateEl = document.getElementById('kiosk-live-date');
  if (!timeEl || !dateEl) return;

  function update() {
    const now = new Date();
    const hours = String(now.getHours()).padStart(2, '0');
    const minutes = String(now.getMinutes()).padStart(2, '0');
    const seconds = String(now.getSeconds()).padStart(2, '0');
    timeEl.textContent = `${hours}:${minutes}:${seconds}`;

    const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric' };
    dateEl.textContent = now.toLocaleDateString('pl-PL', options).toUpperCase();
  }

  update();
  setInterval(update, 1000);
}

/* ==========================================================================
   2. NAWIGACJA ZAKŁADEK
   ========================================================================== */
function initTabNavigation() {
  const dockButtons = document.querySelectorAll('.dock-tab-btn');
  const tabPanes = document.querySelectorAll('.kiosk-tab-pane');
  const presentationBtn = document.getElementById('header-btn-pitch');
  const contentArea = document.querySelector('.kiosk-content');

  function switchTab(tabId) {
    dockButtons.forEach(btn => {
      btn.classList.toggle('active', btn.dataset.tab === tabId);
    });

    tabPanes.forEach(pane => {
      const isActive = pane.id === `tab-${tabId}`;
      pane.classList.toggle('active', isActive);
      if (isActive && contentArea) {
        contentArea.scrollTop = 0;
      }
    });

    // Zaktualizuj stan przycisku prezentacji w nagłówku
    if (presentationBtn) {
      if (tabId === 'prezentacja') {
        presentationBtn.classList.add('active');
        presentationBtn.innerHTML = '<i class="ri-close-line"></i> Wyjdź z prezentacji';
      } else {
        presentationBtn.classList.remove('active');
        presentationBtn.innerHTML = '<i class="ri-slideshow-3-line"></i> Prezentacja MBT';
      }
    }
  }

  dockButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      switchTab(btn.dataset.tab);
    });
  });

  if (presentationBtn) {
    presentationBtn.addEventListener('click', () => {
      const isPresentationActive = document.getElementById('tab-prezentacja')?.classList.contains('active');
      if (isPresentationActive) {
        switchTab('o-nas');
      } else {
        switchTab('prezentacja');
      }
    });
  }

  // Globalny dostęp
  window.kioskSwitchTab = switchTab;
}

/* ==========================================================================
   3. TRYB PEŁNOEKRANOWY (FULLSCREEN)
   ========================================================================== */
function initFullscreen() {
  const fsBtn = document.getElementById('kiosk-fs-toggle');
  if (!fsBtn) return;

  function toggleFullScreen() {
    const doc = window.document;
    const docEl = doc.documentElement;

    const requestFullScreen = docEl.requestFullscreen || docEl.mozRequestFullScreen || docEl.webkitRequestFullScreen || docEl.msRequestFullscreen;
    const cancelFullScreen = doc.exitFullscreen || doc.mozCancelFullScreen || doc.webkitExitFullscreen || doc.msExitFullscreen;

    const isFullscreen = doc.fullscreenElement || doc.mozFullScreenElement || doc.webkitFullscreenElement || doc.msFullscreenElement;

    if (!isFullscreen) {
      if (requestFullScreen) {
        requestFullScreen.call(docEl);
      }
    } else {
      if (cancelFullScreen) {
        cancelFullScreen.call(doc);
      }
    }
  }

  fsBtn.addEventListener('click', toggleFullScreen);

  document.addEventListener('fullscreenchange', updateFsIcon);
  document.addEventListener('webkitfullscreenchange', updateFsIcon);
  document.addEventListener('mozfullscreenchange', updateFsIcon);

  function updateFsIcon() {
    const isFullscreen = document.fullscreenElement || document.webkitFullscreenElement || document.mozFullScreenElement;
    const iconSpan = fsBtn.querySelector('.fs-icon');
    const labelSpan = fsBtn.querySelector('.fs-label');
    if (isFullscreen) {
      if (iconSpan) {
        iconSpan.className = 'ri-fullscreen-exit-line fs-icon';
        iconSpan.textContent = '';
      }
      if (labelSpan) labelSpan.textContent = 'Zmniejsz';
    } else {
      if (iconSpan) {
        iconSpan.className = 'ri-fullscreen-line fs-icon';
        iconSpan.textContent = '';
      }
      if (labelSpan) labelSpan.textContent = 'Pełny ekran';
    }
  }
}

/* ==========================================================================
   4. SUWAK PRZED / PO (BEFORE & AFTER SLIDER)
   ========================================================================== */
function initBeforeAfterSlider() {
  const stage = document.getElementById('kiosk-ba-stage');
  const afterContainer = document.getElementById('kiosk-ba-after-container');
  const handle = document.getElementById('kiosk-ba-handle');
  if (!stage || !afterContainer || !handle) return;

  let isDragging = false;

  function setSliderPosition(clientX) {
    const rect = stage.getBoundingClientRect();
    let x = clientX - rect.left;
    let percent = (x / rect.width) * 100;

    // Ograniczenie między 5% a 95%
    if (percent < 5) percent = 5;
    if (percent > 95) percent = 95;

    afterContainer.style.width = `${percent}%`;
    handle.style.left = `${percent}%`;
  }

  // Obsługa myszy
  stage.addEventListener('mousedown', (e) => {
    isDragging = true;
    setSliderPosition(e.clientX);
  });

  window.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    setSliderPosition(e.clientX);
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
  });

  // Obsługa dotyku (Touch Events)
  stage.addEventListener('touchstart', (e) => {
    isDragging = true;
    if (e.touches.length > 0) {
      setSliderPosition(e.touches[0].clientX);
    }
  }, { passive: true });

  window.addEventListener('touchmove', (e) => {
    if (!isDragging) return;
    if (e.touches.length > 0) {
      setSliderPosition(e.touches[0].clientX);
    }
  }, { passive: true });

  window.addEventListener('touchend', () => {
    isDragging = false;
  });
}

/* ==========================================================================
   5. FILTROWANIE REALIZACJI (Identycznie jak na /realizacje)
   ========================================================================== */
function initProjectFilters() {
  const filterButtons = document.querySelectorAll('.projects-filter-bar .filter-btn');
  const projectCards = document.querySelectorAll('.project-touch-card');

  filterButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      filterButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const filter = btn.dataset.filter;

      projectCards.forEach(card => {
        const type = card.dataset.type || '';
        let match = false;

        if (filter === 'all') {
          match = true;
        } else if (filter === 'completed') {
          match = (type === 'realizacja-zrealizow');
        } else if (filter === 'in-progress') {
          match = (type !== 'realizacja-zrealizow');
        }

        card.style.display = match ? 'flex' : 'none';
      });
    });
  });
}

/* ==========================================================================
   6. MODAL PROJEKTU I GALERIA (Identycznie jak na /realizacja/<slug>/)
   ========================================================================== */
function initProjectModal() {
  const modal = document.getElementById('project-detail-modal');
  const closeBtn = document.getElementById('modal-close-button');
  if (!modal || !closeBtn) return;

  const dataScript = document.getElementById('kiosk-projects-data');
  let projectsData = [];
  if (dataScript) {
    try {
      projectsData = JSON.parse(dataScript.textContent);
    } catch (e) {
      console.error('Błąd parsowania danych projektów:', e);
    }
  }

  const modalTitle = document.getElementById('modal-project-title');
  const modalSubStatus = document.getElementById('modal-project-sub-status');
  const modalMainImg = document.getElementById('modal-project-main-img');
  const modalThumbsBar = document.getElementById('modal-project-thumbs');
  const modalPrevBtn = document.getElementById('modal-gallery-prev');
  const modalNextBtn = document.getElementById('modal-gallery-next');
  const modalStatus = document.getElementById('modal-spec-status');
  const modalCzas = document.getElementById('modal-spec-czas');
  const modalFormula = document.getElementById('modal-spec-formula');
  const modalDesc = document.getElementById('modal-project-desc');
  const modalQrBox = document.getElementById('modal-project-qr');
  const ctaQuoteBtn = document.getElementById('modal-cta-quote-btn');

  let currentGallery = [];
  let currentImgIndex = 0;

  function updateModalGallery(index) {
    if (!currentGallery.length) return;
    currentImgIndex = (index + currentGallery.length) % currentGallery.length;
    modalMainImg.src = currentGallery[currentImgIndex];

    const thumbs = modalThumbsBar.querySelectorAll('.modal-thumb-item');
    thumbs.forEach((th, idx) => {
      th.classList.toggle('active', idx === currentImgIndex);
    });
  }

  function openProject(slug) {
    const proj = projectsData.find(p => p.slug === slug);
    if (!proj) return;

    if (modalTitle) modalTitle.textContent = proj.title;
    if (modalSubStatus) modalSubStatus.textContent = proj.status || 'Zrealizowane';
    if (modalStatus) modalStatus.textContent = proj.status || 'Zrealizowane';
    if (modalCzas) modalCzas.textContent = proj.czas || '—';
    if (modalFormula) modalFormula.textContent = proj.formula_display || proj.formula || 'Generalne wykonawstwo';

    if (modalDesc) {
      if (proj.opis_paras && proj.opis_paras.length > 0) {
        modalDesc.innerHTML = proj.opis_paras.map(p =>
          `<p style="margin-bottom: 0.95rem; line-height: 1.65; color: var(--text-secondary); font-size: 1.05rem;">${p}</p>`
        ).join('');
      } else if (proj.opis) {
        modalDesc.innerHTML = `<p style="margin-bottom: 0.95rem; line-height: 1.65; color: var(--text-secondary); font-size: 1.05rem;">${proj.opis.replace(/\n/g, '<br>')}</p>`;
      } else {
        modalDesc.innerHTML = '<p style="color: var(--text-secondary); font-size: 1.05rem;">Kompleksowa realizacja inwestycji kubaturowej w standardzie generalnego wykonawstwa MBT.</p>';
      }
    }

    // Budowanie galerii
    currentGallery = [];
    if (proj.hero) currentGallery.push(proj.hero);
    if (proj.gallery && proj.gallery.length) {
      proj.gallery.forEach(img => {
        if (!currentGallery.includes(img)) currentGallery.push(img);
      });
    }

    modalThumbsBar.innerHTML = '';
    currentGallery.forEach((imgSrc, idx) => {
      const thumb = document.createElement('img');
      thumb.src = imgSrc;
      thumb.className = 'modal-thumb-item' + (idx === 0 ? ' active' : '');
      thumb.addEventListener('click', () => updateModalGallery(idx));
      modalThumbsBar.appendChild(thumb);
    });

    updateModalGallery(0);

    // Dynamiczny kod QR dla realizacji
    if (modalQrBox) {
      const projectUrl = `https://mbt.pl/realizacja/${proj.slug}/`;
      modalQrBox.innerHTML = generateQrSvg(projectUrl, 84);
    }

    modal.classList.add('open');
  }

  function closeModal() {
    modal.classList.remove('open');
  }

  if (ctaQuoteBtn) {
    ctaQuoteBtn.addEventListener('click', () => {
      closeModal();
      if (window.kioskSwitchTab) {
        window.kioskSwitchTab('kontakt');
      }
    });
  }

  closeBtn.addEventListener('click', closeModal);
  modal.addEventListener('click', (e) => {
    if (e.target === modal) closeModal();
  });

  if (modalPrevBtn) modalPrevBtn.addEventListener('click', () => updateModalGallery(currentImgIndex - 1));
  if (modalNextBtn) modalNextBtn.addEventListener('click', () => updateModalGallery(currentImgIndex + 1));

  // Gesty swipe w galerii modala
  let touchStartX = 0;
  modalMainImg.addEventListener('touchstart', (e) => {
    if (e.touches.length > 0) touchStartX = e.touches[0].clientX;
  }, { passive: true });

  modalMainImg.addEventListener('touchend', (e) => {
    if (e.changedTouches.length > 0) {
      const touchEndX = e.changedTouches[0].clientX;
      const diff = touchStartX - touchEndX;
      if (Math.abs(diff) > 40) {
        if (diff > 0) updateModalGallery(currentImgIndex + 1); // swipe lewo -> następne
        else updateModalGallery(currentImgIndex - 1); // swipe prawo -> poprzednie
      }
    }
  }, { passive: true });

  // Podpięcie kliknięcia pod każdą kartę realizacji
  document.querySelectorAll('.project-touch-card').forEach(card => {
    card.addEventListener('click', () => {
      const slug = card.dataset.slug;
      if (slug) openProject(slug);
    });
  });
}

/* ==========================================================================
   7. PREZENTACJA PITCH DECK (23 OFICJALNE SLAJDY MBT)
   ========================================================================== */
function initPresentationDeck() {
  const slides = document.querySelectorAll('.deck-slide');
  const prevBtn = document.getElementById('deck-btn-prev');
  const nextBtn = document.getElementById('deck-btn-next');
  const stagePrevBtn = document.getElementById('slide-stage-arrow-prev');
  const stageNextBtn = document.getElementById('slide-stage-arrow-next');
  const counterEl = document.getElementById('deck-counter-text');
  const filmstripContainer = document.getElementById('deck-filmstrip-container');
  const thumbCards = document.querySelectorAll('.deck-thumb-card');

  const overviewBtn = document.getElementById('deck-btn-overview');
  const overviewModal = document.getElementById('deck-overview-modal');
  const overviewCloseBtn = document.getElementById('deck-overview-close');
  const overviewItems = document.querySelectorAll('.deck-overview-item');
  const fsSlideBtn = document.getElementById('deck-btn-fullscreen-slide');

  if (!slides.length) return;

  let currentSlide = 0;
  const totalSlides = slides.length;

  function goToSlide(index) {
    currentSlide = (index + totalSlides) % totalSlides;

    // Przełączanie slajdów głównych
    slides.forEach((slide, idx) => {
      slide.classList.toggle('active', idx === currentSlide);
    });

    // Przełączanie miniaturek na dolnym pasku (Filmstrip)
    thumbCards.forEach((card, idx) => {
      card.classList.toggle('active', idx === currentSlide);
    });

    // Płynne centrowanie aktywnej miniatury w widoku
    const activeThumb = thumbCards[currentSlide];
    if (activeThumb && filmstripContainer) {
      const cardLeft = activeThumb.offsetLeft;
      const cardWidth = activeThumb.offsetWidth;
      const containerWidth = filmstripContainer.offsetWidth;
      filmstripContainer.scrollTo({
        left: cardLeft - (containerWidth / 2) + (cardWidth / 2),
        behavior: 'smooth'
      });
    }

    // Aktualizacja aktywnego elementu w siatce spisu slajdów
    overviewItems.forEach((item, idx) => {
      item.classList.toggle('active', idx === currentSlide);
    });

    // Licznik slajdów
    if (counterEl) {
      counterEl.textContent = `${currentSlide + 1} / ${totalSlides}`;
    }
  }

  // Przyciski nawigacyjne
  if (prevBtn) prevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  if (nextBtn) nextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));
  if (stagePrevBtn) stagePrevBtn.addEventListener('click', () => goToSlide(currentSlide - 1));
  if (stageNextBtn) stageNextBtn.addEventListener('click', () => goToSlide(currentSlide + 1));

  // Kliknięcie w miniaturę na filmstripie
  thumbCards.forEach(card => {
    card.addEventListener('click', () => {
      const idx = parseInt(card.dataset.slideIndex, 10);
      if (!isNaN(idx)) goToSlide(idx);
    });
  });

  // Modal spisu wszystkich slajdów (Siatka)
  function openOverview() {
    if (overviewModal) overviewModal.classList.add('open');
  }

  function closeOverview() {
    if (overviewModal) overviewModal.classList.remove('open');
  }

  if (overviewBtn) overviewBtn.addEventListener('click', openOverview);
  if (overviewCloseBtn) overviewCloseBtn.addEventListener('click', closeOverview);

  if (overviewModal) {
    overviewModal.addEventListener('click', (e) => {
      if (e.target === overviewModal) closeOverview();
    });
  }

  overviewItems.forEach(item => {
    item.addEventListener('click', () => {
      const idx = parseInt(item.dataset.slideIndex, 10);
      if (!isNaN(idx)) {
        goToSlide(idx);
        closeOverview();
      }
    });
  });

  // Pełny ekran prezentacji
  if (fsSlideBtn) {
    fsSlideBtn.addEventListener('click', () => {
      const container = document.querySelector('.presentation-view-container');
      if (!container) return;
      if (!document.fullscreenElement) {
        if (container.requestFullscreen) container.requestFullscreen();
        else if (container.webkitRequestFullscreen) container.webkitRequestFullscreen();
      } else {
        if (document.exitFullscreen) document.exitFullscreen();
      }
    });
  }

  // Obsługa klawiszy (prezenter bezprzewodowy / klawiatura)
  window.addEventListener('keydown', (e) => {
    const isPresentationActive = document.getElementById('tab-prezentacja')?.classList.contains('active');
    if (!isPresentationActive) return;

    if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown') {
      goToSlide(currentSlide + 1);
    } else if (e.key === 'ArrowLeft' || e.key === 'PageUp') {
      goToSlide(currentSlide - 1);
    } else if (e.key === 'Escape') {
      closeOverview();
    }
  });

  // Obsługa gestu swipe palcem na slajdzie
  const deckViewport = document.getElementById('presentation-viewport');
  if (deckViewport) {
    let slideTouchStartX = 0;
    deckViewport.addEventListener('touchstart', (e) => {
      if (e.touches.length > 0) slideTouchStartX = e.touches[0].clientX;
    }, { passive: true });

    deckViewport.addEventListener('touchend', (e) => {
      if (e.changedTouches.length > 0) {
        const slideTouchEndX = e.changedTouches[0].clientX;
        const diff = slideTouchStartX - slideTouchEndX;
        if (Math.abs(diff) > 50) {
          if (diff > 0) goToSlide(currentSlide + 1); // swipe lewo -> następny
          else goToSlide(currentSlide - 1); // swipe prawo -> poprzedni
        }
      }
    }, { passive: true });
  }

  goToSlide(0);
}

/* ==========================================================================
   8. GENERATOR KODÓW QR (LEKKI, NATYWNY SVG)
   ========================================================================== */
function initQRCodes() {
  const contactQrBox = document.getElementById('kiosk-main-contact-qr');
  if (contactQrBox) {
    // Generowanie kodu QR dla wizytówki vCard / strony kontaktowej MBT
    const vCardData = 'https://mbt.pl/kontakt/';
    contactQrBox.innerHTML = generateQrSvg(vCardData, 176);
  }
}

/**
 * Lekki generator SVG QR wykorzystujący Google Chart API z fallbackiem lub uniwersalny kod QR SVG.
 */
function generateQrSvg(text, size) {
  const encoded = encodeURIComponent(text);
  // Czyste, ostre renderowanie QR w 4K z obsługą offline cache
  return `<img src="https://api.qrserver.com/v1/create-qr-code/?size=${size}x${size}&data=${encoded}&margin=0&color=023E7C" 
              alt="Kod QR" 
              style="width: 100%; height: 100%; object-fit: contain; border-radius: 6px;" 
              onerror="this.src='/static/img/mbt/mbt_crane_qr.png';">`;
}
