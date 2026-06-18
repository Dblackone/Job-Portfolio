/* ===================================================================
   VOLLMANN — Motion Portfolio (v2)  ·  vanilla JS
   Reveals (IntersectionObserver) · magnetic hover (pointer + rAF) ·
   kinetic marquee + sticky-stack scaling (rAF-batched passive scroll) ·
   char-split about text. All motion respects prefers-reduced-motion.
   =================================================================== */
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const finePointer = window.matchMedia('(hover:hover) and (pointer:fine)').matches;
  const enc = (p) => encodeURI(p);
  const A = 'assets/Project Pictures/';

  /* ── DATA ─────────────────────────────────────────────────────── */
  const MARQUEE = [
    [ // row 1 (moves one way)
      A+'Landscape Projects/Estate Aerial Hero.png',
      A+'Ado Hall of Worship/Ado Hero 2.png',
      A+'Hillside Project/HERO IMG.png',
      A+'Uselu Family house/Usele Hero 1.png',
      A+'6-flat ikotun lagos/Chinedu Hero Render.png',
      A+'Other Renders/Event Hall.png',
      A+'Interior Residential Operations/RENDER 2.png',
    ],
    [ // row 2 (moves the other way)
      A+'Renovation Akure/Akure Family Home.png',
      A+'Other Renders/Entrance Gatehouse.png',
      A+'Interior Residential Operations/RENDER 1.png',
      A+'Interior Residential Operations/Bathroom Suite.png',
      A+'Interior Residential Operations/Executive Boardroom.jpeg',
      A+'Landscape Projects/Video1 - Snapshot7_003.jpg',
    ],
  ];

  const PROJECTS = [
    { num:'01', cat:'Religious · Built', name:'Hall of Worship, Ado',
      a:A+'Ado Hall of Worship/Image8_005.png',
      b:A+'Ado Hall of Worship/ADO CENTER RAW 1.jpg',
      tall:A+'Ado Hall of Worship/Ado Hero 2.png' },
    { num:'02', cat:'Residential · Concept', name:'The Hillside Project',
      a:A+'Hillside Project/RAW 1.jpg',
      b:A+'Hillside Project/02 Detail Study.png',
      tall:A+'Hillside Project/HERO IMG.png' },
    { num:'03', cat:'Residential · Built', name:'4-Bedroom Family House, Uselu',
      a:A+'Uselu Family house/USELU - NIGHT VIEW.png',
      b:A+'Uselu Family house/USELU - COLAGE.png',
      tall:A+'Uselu Family house/Usele Hero 1.png' },
  ];

  const PDF = 'assets/vollmann-akarakiri-portfolio.pdf';

  document.addEventListener('DOMContentLoaded', () => {

    /* ── render marquee ─────────────────────────────────────────── */
    const tile = (src) => {
      const d = document.createElement('div'); d.className = 'marquee-tile';
      const img = document.createElement('img');
      img.src = enc(src); img.alt = ''; img.loading = 'lazy';
      d.appendChild(img); return d;
    };
    const rows = document.querySelectorAll('.marquee-row');
    MARQUEE.forEach((list, i) => {
      const row = rows[i]; if (!row) return;
      const tripled = [...list, ...list, ...list];
      tripled.forEach(src => row.appendChild(tile(src)));
    });

    /* ── render project cards ───────────────────────────────────── */
    const stack = document.querySelector('.proj-stack');
    if (stack) {
      PROJECTS.forEach((p, i) => {
        const card = document.createElement('article');
        card.className = 'proj-card';
        card.style.top = `calc(88px + ${i} * 26px)`;
        card.innerHTML = `
          <div class="proj-top">
            <div class="proj-num">${p.num}</div>
            <div class="proj-meta">
              <span class="proj-cat">${p.cat}</span>
              <span class="proj-name">${p.name}</span>
            </div>
            <a class="btn-ghost" href="${PDF}" target="_blank" rel="noopener">View Project</a>
          </div>
          <div class="proj-grid">
            <div class="proj-col">
              <img class="pa" src="${enc(p.a)}" alt="" loading="lazy" />
              <img class="pb" src="${enc(p.b)}" alt="" loading="lazy" />
            </div>
            <img class="proj-tall" src="${enc(p.tall)}" alt="" loading="lazy" />
          </div>`;
        stack.appendChild(card);
      });
    }

    /* ── split about text into characters ───────────────────────── */
    const aboutText = document.querySelector('.about-text');
    if (aboutText) {
      const txt = aboutText.textContent.trim();
      aboutText.textContent = '';
      [...txt].forEach((c, i) => {
        const s = document.createElement('span');
        s.className = 'ch'; s.style.setProperty('--cd', (i * 0.012) + 's');
        s.textContent = c;
        aboutText.appendChild(s);
      });
    }

    /* ── scroll reveals + about stagger (IntersectionObserver) ──── */
    const io = new IntersectionObserver((entries) => {
      entries.forEach(e => { if (e.isIntersecting){ e.target.classList.add('is-in'); io.unobserve(e.target); } });
    }, { threshold:0.15, rootMargin:'0px 0px -8% 0px' });
    document.querySelectorAll('[data-reveal], .about-text').forEach(el => io.observe(el));

    /* ── nav state ──────────────────────────────────────────────── */
    const nav = document.getElementById('nav');
    const darkSecs = [...document.querySelectorAll('.dark-sec')];
    const navOnDark = () => {
      const probe = 34; // mid-nav line
      return darkSecs.some(s => { const r = s.getBoundingClientRect(); return r.top <= probe && r.bottom >= probe; });
    };

    /* ── magnetic hover (pointer-driven, rAF) ───────────────────── */
    if (finePointer && !reduce) {
      document.querySelectorAll('[data-magnet]').forEach(el => {
        const strength = parseFloat(el.dataset.magnet) || 3;
        const pad = 130; let raf = null, tx = 0, ty = 0;
        const apply = () => { el.style.transform = `translate3d(${tx}px,${ty}px,0)`; raf = null; };
        el.closest('.magnet-area, body').addEventListener('pointermove', (e) => {
          const r = el.getBoundingClientRect();
          const cx = r.left + r.width/2, cy = r.top + r.height/2;
          const dx = e.clientX - cx, dy = e.clientY - cy;
          const within = Math.abs(dx) < r.width/2 + pad && Math.abs(dy) < r.height/2 + pad;
          el.style.transition = 'transform .3s ease-out';
          tx = within ? dx/strength : 0; ty = within ? dy/strength : 0;
          if (!raf) raf = requestAnimationFrame(apply);
        });
        el.addEventListener('pointerleave', () => {
          el.style.transition = 'transform .6s ease-in-out'; tx = ty = 0;
          if (!raf) raf = requestAnimationFrame(apply);
        });
      });
    }

    /* ── rAF-batched scroll: nav, marquee, sticky-stack scale ───── */
    const marquee = document.querySelector('.marquee');
    const r1 = rows[0], r2 = rows[1];
    let thirds = [0, 0];
    const measure = () => { thirds = [ r1 ? r1.scrollWidth/3 : 0, r2 ? r2.scrollWidth/3 : 0 ]; };
    measure(); window.addEventListener('resize', measure, { passive:true });

    const cards = () => [...document.querySelectorAll('.proj-card')];
    let ticking = false;
    const frame = () => {
      ticking = false;
      const y = window.scrollY;
      // nav
      nav.classList.toggle('scrolled', y > 40);
      nav.classList.toggle('on-dark', navOnDark());

      if (reduce) return;
      // marquee — opposite-direction drift tied to scroll position
      if (marquee && r1 && r2){
        const mr = marquee.getBoundingClientRect();
        const off = (window.innerHeight - mr.top) * 0.16;
        r1.style.transform = `translate3d(${(-thirds[0] + off).toFixed(1)}px,0,0)`;
        r2.style.transform = `translate3d(${(-thirds[1] - off).toFixed(1)}px,0,0)`;
      }
      // sticky-stack: shrink/dim a card as the next one rises over it
      const cs = cards(); const n = cs.length;
      cs.forEach((card, i) => {
        if (i === n - 1) return;
        const next = cs[i + 1].getBoundingClientRect();
        const start = window.innerHeight;     // next card enters from bottom
        const end = (parseFloat(card.style.top) || 96); // until it overlaps
        const p = Math.min(1, Math.max(0, (start - next.top) / (start - end)));
        const target = 1 - (n - 1 - i) * 0.04;
        const scale = 1 - p * (1 - target);
        card.style.transform = `scale(${scale.toFixed(3)})`;
        card.style.opacity = (1 - p * 0.25).toFixed(3);
      });
    };
    const onScroll = () => { if (!ticking){ ticking = true; requestAnimationFrame(frame); } };
    window.addEventListener('scroll', onScroll, { passive:true });
    // initial paint (after images may shift layout)
    frame(); window.addEventListener('load', () => { measure(); frame(); });

    /* ── smooth anchor scroll ───────────────────────────────────── */
    document.querySelectorAll('a[href^="#"]').forEach(a => {
      a.addEventListener('click', (e) => {
        const t = document.querySelector(a.getAttribute('href'));
        if (t){ e.preventDefault(); t.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block:'start' }); }
      });
    });

    /* ── footer year ────────────────────────────────────────────── */
    const yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();
  });
})();
