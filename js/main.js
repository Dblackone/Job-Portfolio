/* ===================================================================
   AKARAKIRI PORTFOLIO SYSTEM — main.js
   Interactions: scroll, nav, reveal animations, mobile menu
   =================================================================== */

document.addEventListener('DOMContentLoaded', () => {

  // ── PROGRESS BAR ──────────────────────────────────────────────
  const progress = document.getElementById('progress');
  const updateProgress = () => {
    const scrolled = window.scrollY;
    const total = document.body.scrollHeight - window.innerHeight;
    progress.style.width = `${(scrolled / total) * 100}%`;
  };

  // ── NAV SCROLL BEHAVIOUR ───────────────────────────────────────
  const nav = document.getElementById('nav');
  const backTop = document.getElementById('back-top');
  const navLinks = document.querySelectorAll('.nav-links a');

  const onScroll = () => {
    const y = window.scrollY;
    nav.classList.toggle('scrolled', y > 40);
    backTop.classList.toggle('visible', y > 500);
    updateProgress();
    highlightNav();
    revealElements();
  };

  // ── ACTIVE NAV HIGHLIGHTING ────────────────────────────────────
  const sections = document.querySelectorAll('section[id]');
  const highlightNav = () => {
    let current = '';
    sections.forEach(section => {
      if (window.scrollY >= section.offsetTop - 120) current = section.id;
    });
    navLinks.forEach(link => {
      link.classList.toggle('active', link.getAttribute('href') === `#${current}`);
    });
  };

  // ── SCROLL REVEAL ──────────────────────────────────────────────
  const revealEls = document.querySelectorAll('[data-reveal]');
  const revealElements = () => {
    revealEls.forEach(el => {
      const rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight - 80) el.classList.add('revealed');
    });
  };
  revealElements(); // initial check

  window.addEventListener('scroll', onScroll, { passive: true });

  // ── BACK TO TOP ────────────────────────────────────────────────
  backTop.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

  // ── MOBILE MENU ────────────────────────────────────────────────
  const burger = document.getElementById('burger');
  const mobileMenu = document.getElementById('mobile-menu');
  const mobileLinks = mobileMenu.querySelectorAll('a');

  const toggleMenu = (open) => {
    burger.classList.toggle('open', open);
    mobileMenu.classList.toggle('open', open);
    document.body.style.overflow = open ? 'hidden' : '';
  };

  burger.addEventListener('click', () => toggleMenu(!burger.classList.contains('open')));
  mobileLinks.forEach(link => link.addEventListener('click', () => toggleMenu(false)));

  // ── SMOOTH SCROLL FOR ANCHOR LINKS ────────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }
    });
  });

  // ── HERO HEADLINE TYPEWRITER EFFECT ───────────────────────────
  const lines = document.querySelectorAll('.hero-headline .line');
  lines.forEach((line, i) => {
    line.style.opacity = '0';
    line.style.transform = 'translateY(24px)';
    line.style.transition = `opacity 0.7s ease ${i * 0.15 + 0.2}s, transform 0.7s ease ${i * 0.15 + 0.2}s`;
    requestAnimationFrame(() => {
      setTimeout(() => {
        line.style.opacity = '1';
        line.style.transform = 'translateY(0)';
      }, 50);
    });
  });

  // Hero actions
  const heroActions = document.querySelector('.hero-actions');
  if (heroActions) {
    heroActions.style.opacity = '0';
    heroActions.style.transform = 'translateY(16px)';
    heroActions.style.transition = 'opacity 0.7s ease 0.85s, transform 0.7s ease 0.85s';
    setTimeout(() => {
      heroActions.style.opacity = '1';
      heroActions.style.transform = 'translateY(0)';
    }, 50);
  }

  // ── PORTFOLIO CARD HOVER RIPPLE ────────────────────────────────
  document.querySelectorAll('.portfolio-card, .project-card').forEach(card => {
    card.addEventListener('mouseenter', function(e) {
      const rect = this.getBoundingClientRect();
      const x = e.clientX - rect.left;
      const y = e.clientY - rect.top;
      this.style.setProperty('--ripple-x', `${x}px`);
      this.style.setProperty('--ripple-y', `${y}px`);
    });
  });

  // ── CURRENT YEAR IN FOOTER ─────────────────────────────────────
  const yearEl = document.getElementById('year');
  if (yearEl) yearEl.textContent = new Date().getFullYear();

});
