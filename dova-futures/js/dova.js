/* DOVA Futures — site interactions */

/* ── Page routing ─────────────────────────────────────────────── */
function navigate(page) {
  document.querySelectorAll('.page').forEach(p => {
    p.style.display = p.dataset.page === page ? 'block' : 'none';
  });
  document.querySelectorAll('[data-navlink]').forEach(a => {
    a.classList.toggle('active', a.dataset.navlink === page);
  });
  window.scrollTo({ top: 0, behavior: 'smooth' });
  // Re-observe reveal elements on new page
  setupReveal();
}

// Wire all [data-go] elements
function wireNav() {
  document.querySelectorAll('[data-go]').forEach(el => {
    el.addEventListener('click', (e) => {
      e.preventDefault();
      navigate(el.dataset.go);
    });
  });
}

/* ── Before/after reveal slider ──────────────────────────────── */
function setupSlider() {
  const slider = document.getElementById('hero-slider');
  if (!slider) return;

  const handle   = document.getElementById('slider-handle');
  const draftWrap = slider.querySelector('.hero__img-draft-wrap');
  let dragging = false;
  let split = 52;

  function updateSlider(clientX) {
    const r = slider.getBoundingClientRect();
    split = Math.max(6, Math.min(94, (clientX - r.left) / r.width * 100));
    draftWrap.style.clipPath = `inset(0 ${100 - split}% 0 0)`;
    handle.style.left = `${split}%`;
  }

  handle.addEventListener('mousedown',  () => { dragging = true; });
  handle.addEventListener('touchstart', () => { dragging = true; }, { passive: true });

  window.addEventListener('mouseup',  () => { dragging = false; });
  window.addEventListener('touchend', () => { dragging = false; });

  window.addEventListener('mousemove', (e) => {
    if (!dragging) return;
    updateSlider(e.clientX);
  });
  window.addEventListener('touchmove', (e) => {
    if (!dragging) return;
    updateSlider(e.touches[0].clientX);
  }, { passive: true });
}

/* ── Scroll-reveal ────────────────────────────────────────────── */
let revealObserver;

function setupReveal() {
  if (revealObserver) revealObserver.disconnect();

  revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -48px 0px' });

  // Only observe elements inside the currently visible page
  const activePage = document.querySelector('.page[data-page]:not([style*="display: none"])') ||
                     document.querySelector('.page[data-page]');
  if (!activePage) return;

  activePage.querySelectorAll('.reveal:not(.revealed)').forEach(el => {
    revealObserver.observe(el);
  });
}

/* ── Projects filter ──────────────────────────────────────────── */
function setupFilter() {
  const btns = document.querySelectorAll('.filter-btn');
  if (!btns.length) return;

  btns.forEach(btn => {
    btn.addEventListener('click', () => {
      btns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const cat = btn.dataset.cat;
      document.querySelectorAll('.project-item').forEach(item => {
        const show = cat === 'All' || item.dataset.category === cat;
        item.style.display = show ? 'block' : 'none';
      });
    });
  });
}

/* ── Contact form ─────────────────────────────────────────────── */
function setupForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();
    document.getElementById('form-thanks').style.display = 'block';
    form.style.display = 'none';
  });
}

/* ── Nav scroll shadow ────────────────────────────────────────── */
function setupNavShadow() {
  const nav = document.querySelector('.nav');
  if (!nav) return;
  window.addEventListener('scroll', () => {
    nav.style.boxShadow = window.scrollY > 10 ? '0 2px 24px rgba(11,34,26,0.4)' : 'none';
  }, { passive: true });
}

/* ── Init ─────────────────────────────────────────────────────── */
document.addEventListener('DOMContentLoaded', () => {
  wireNav();
  setupSlider();
  setupReveal();
  setupFilter();
  setupForm();
  setupNavShadow();

  // Show home page by default
  navigate('home');
});
