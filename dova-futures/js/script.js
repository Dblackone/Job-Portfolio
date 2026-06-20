// ─── Lucide icons ───
document.addEventListener('DOMContentLoaded', () => {
  if (window.lucide) lucide.createIcons()
})

// ─── Scroll-reveal (IntersectionObserver) ───
function initFadeIn() {
  const els = document.querySelectorAll('[data-fade]')

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return
        const el = entry.target
        const delay = parseFloat(el.dataset.delay || '0')
        el.style.transitionDelay = `${delay}s`
        el.classList.add('is-visible')
        observer.unobserve(el)
      })
    },
    { rootMargin: '0px 0px -60px 0px', threshold: 0.08 }
  )

  els.forEach((el) => observer.observe(el))
}

// ─── Mobile nav ───
function initMobileNav() {
  const hamburger = document.getElementById('hamburger')
  const mobileMenu = document.getElementById('mobile-menu')
  if (!hamburger || !mobileMenu) return

  hamburger.addEventListener('click', () => {
    const isOpen = mobileMenu.classList.toggle('is-open')
    hamburger.setAttribute('aria-expanded', String(isOpen))
    const spans = hamburger.querySelectorAll('span')
    if (isOpen) {
      spans[0].style.transform = 'translateY(7px) rotate(45deg)'
      spans[1].style.opacity = '0'
      spans[2].style.transform = 'translateY(-7px) rotate(-45deg)'
    } else {
      spans[0].style.transform = ''
      spans[1].style.opacity = ''
      spans[2].style.transform = ''
    }
  })

  // Close on link click
  mobileMenu.querySelectorAll('a').forEach((a) => {
    a.addEventListener('click', () => {
      mobileMenu.classList.remove('is-open')
      hamburger.setAttribute('aria-expanded', 'false')
      const spans = hamburger.querySelectorAll('span')
      spans[0].style.transform = ''
      spans[1].style.opacity = ''
      spans[2].style.transform = ''
    })
  })
}

// ─── Before/After reveal slider ───
function initRevealSlider() {
  const slider = document.getElementById('reveal-slider')
  const beforeInner = document.getElementById('slider-before-inner')
  const divider = document.getElementById('slider-divider')
  const handle = document.getElementById('slider-handle')
  if (!slider || !beforeInner) return

  let dragging = false
  let pct = 50

  function setPosition(x) {
    const rect = slider.getBoundingClientRect()
    let p = ((x - rect.left) / rect.width) * 100
    p = Math.max(2, Math.min(98, p))
    pct = p
    beforeInner.style.width = `${p}%`
    divider.style.left = `${p}%`
    handle.style.left = `${p}%`
  }

  slider.addEventListener('mousedown', (e) => {
    dragging = true
    setPosition(e.clientX)
    e.preventDefault()
  })
  slider.addEventListener('touchstart', (e) => {
    dragging = true
    setPosition(e.touches[0].clientX)
  }, { passive: true })

  window.addEventListener('mousemove', (e) => {
    if (!dragging) return
    setPosition(e.clientX)
  })
  window.addEventListener('touchmove', (e) => {
    if (!dragging) return
    setPosition(e.touches[0].clientX)
  }, { passive: true })

  window.addEventListener('mouseup', () => { dragging = false })
  window.addEventListener('touchend', () => { dragging = false })
}

// ─── Project filter ───
function initProjectFilter() {
  const btns = document.querySelectorAll('.filter-btn')
  const cards = document.querySelectorAll('.project-card')
  if (!btns.length) return

  btns.forEach((btn) => {
    btn.addEventListener('click', () => {
      btns.forEach((b) => b.classList.remove('is-active'))
      btn.classList.add('is-active')

      const filter = btn.dataset.filter

      cards.forEach((card) => {
        const cats = card.dataset.category || ''
        const matches = filter === 'all' || cats.includes(filter)
        card.style.transition = 'opacity 0.3s, transform 0.3s'
        if (matches) {
          card.style.opacity = '1'
          card.style.transform = ''
          card.style.pointerEvents = ''
        } else {
          card.style.opacity = '0.2'
          card.style.transform = 'scale(0.97)'
          card.style.pointerEvents = 'none'
        }
      })
    })
  })
}

// ─── Contact form (stub) ───
function initContactForm() {
  const form = document.getElementById('contact-form')
  const status = document.getElementById('form-status')
  if (!form) return

  form.addEventListener('submit', (e) => {
    e.preventDefault()
    if (status) {
      status.style.display = 'block'
      status.textContent = 'Thank you — we will be in touch within one business day.'
    }
    form.reset()
  })
}

// ─── Smooth nav scroll offset (fixed header) ───
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach((a) => {
    a.addEventListener('click', (e) => {
      const id = a.getAttribute('href').slice(1)
      const target = document.getElementById(id)
      if (!target) return
      e.preventDefault()
      const offset = 80
      const top = target.getBoundingClientRect().top + window.scrollY - offset
      window.scrollTo({ top, behavior: 'smooth' })
    })
  })
}

// ─── Init ───
document.addEventListener('DOMContentLoaded', () => {
  initFadeIn()
  initMobileNav()
  initRevealSlider()
  initProjectFilter()
  initContactForm()
  initSmoothScroll()
})
