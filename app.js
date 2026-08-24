/* ==========================================================================
   X1 LIVE CINEMA QUIZSHOW - CLIENT PRESENTATION ENGINE
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  
  // 1. SCREEN SWITCHER LOGIC
  const navBtns = document.querySelectorAll('.nav-btn');
  const screens = document.querySelectorAll('.cinema-canvas');
  const downloadCurrentBtn = document.getElementById('downloadCurrentBtn');

  const fileMap = {
    'screen1': 'output/Design_01_Smartphone_App.png',
    'screen2': 'output/Design_02_Kino_Leinwand_Moderator_Top20_Top50.png',
    'screen3': 'output/Design_03_Kino_Leinwand_Ankuendigung_Countdown_Top20.png',
    'screen4': 'output/Design_04_Kino_Leinwand_Quizfrage_Quizfilm.png',
    'screen5': 'output/Design_05_Kino_Leinwand_Gewinner_Gesamtstand.png'
  };

  navBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const targetId = btn.getAttribute('data-screen');
      
      navBtns.forEach(b => b.classList.remove('active'));
      screens.forEach(s => s.classList.remove('screen-active'));

      btn.classList.add('active');
      const targetScreen = document.getElementById(targetId);
      if (targetScreen) {
        targetScreen.classList.add('screen-active');
      }

      // Update download link for current active screen
      if (downloadCurrentBtn && fileMap[targetId]) {
        downloadCurrentBtn.setAttribute('href', fileMap[targetId]);
      }
    });
  });

  // 2. STAGE AUTO-ZOOM & FIT ENGINE
  const canvasStage = document.getElementById('canvasStage');
  const viewportWrapper = document.querySelector('.viewport-wrapper');
  const zoomValueText = document.getElementById('zoomValue');
  const zoomInBtn = document.getElementById('zoomInBtn');
  const zoomOutBtn = document.getElementById('zoomOutBtn');
  const resetZoomBtn = document.getElementById('resetZoomBtn');

  let currentScale = 0.3;
  let isAutoFit = true;

  function applyScale(scale) {
    canvasStage.style.transform = `translate(-50%, -50%) scale(${scale})`;
  }

  function fitStageToViewport() {
    if (!isAutoFit) return;
    const padding = 60;
    const availWidth = viewportWrapper.clientWidth - padding;
    const availHeight = viewportWrapper.clientHeight - padding;
    
    const scaleX = availWidth / 4096;
    const scaleY = availHeight / 1716;
    currentScale = Math.min(scaleX, scaleY);
    
    applyScale(currentScale);
    zoomValueText.textContent = `${Math.round(currentScale * 100)}% (FIT)`;
  }

  window.addEventListener('resize', fitStageToViewport);
  fitStageToViewport();

  zoomInBtn.addEventListener('click', () => {
    isAutoFit = false;
    currentScale = Math.min(currentScale + 0.05, 2.0);
    applyScale(currentScale);
    zoomValueText.textContent = `${Math.round(currentScale * 100)}%`;
  });

  zoomOutBtn.addEventListener('click', () => {
    isAutoFit = false;
    currentScale = Math.max(currentScale - 0.05, 0.1);
    applyScale(currentScale);
    zoomValueText.textContent = `${Math.round(currentScale * 100)}%`;
  });

  resetZoomBtn.addEventListener('click', () => {
    isAutoFit = true;
    fitStageToViewport();
  });
});
