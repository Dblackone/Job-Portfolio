// ---------- Data ----------

const marqueeImages = [
  'https://motionsites.ai/assets/hero-space-voyage-preview-eECLH3Yc.gif',
  'https://motionsites.ai/assets/hero-codenest-preview-Cgppc2qV.gif',
  'https://motionsites.ai/assets/hero-vex-ventures-preview-BczMFIiw.gif',
  'https://motionsites.ai/assets/hero-stellar-ai-v2-preview-DjvxjG3C.gif',
  'https://motionsites.ai/assets/hero-asme-preview-B_nGDnTP.gif',
  'https://motionsites.ai/assets/hero-transform-data-preview-Cx5OU29N.gif',
  'https://motionsites.ai/assets/hero-vitara-preview-Cjz2QYyU.gif',
  'https://motionsites.ai/assets/hero-terra-preview-BFjrCr7T.gif',
  'https://motionsites.ai/assets/hero-skyelite-preview-DHaZIgUv.gif',
  'https://motionsites.ai/assets/hero-aethera-preview-DknSlcTa.gif',
  'https://motionsites.ai/assets/hero-designpro-preview-D8c5_een.gif',
  'https://motionsites.ai/assets/hero-stellar-ai-preview-D3HL6bw1.gif',
  'https://motionsites.ai/assets/hero-xportfolio-preview-D4A8maiC.gif',
  'https://motionsites.ai/assets/hero-orbit-web3-preview-BXt4OttD.gif',
  'https://motionsites.ai/assets/hero-nexora-preview-cx5HmUgo.gif',
  'https://motionsites.ai/assets/hero-evr-ventures-preview-DZxeVFEX.gif',
  'https://motionsites.ai/assets/hero-planet-orbit-preview-DWAP8Z1P.gif',
  'https://motionsites.ai/assets/hero-new-era-preview-CocuDUm9.gif',
  'https://motionsites.ai/assets/hero-wealth-preview-B70idl_u.gif',
  'https://motionsites.ai/assets/hero-luminex-preview-CxOP7ce6.gif',
  'https://motionsites.ai/assets/hero-celestia-preview-0yO3jXO8.gif',
]

const marqueeRow1 = marqueeImages.slice(0, 11)
const marqueeRow2 = marqueeImages.slice(11)

const projects = [
  {
    number: '01',
    name: 'Lekki Hillside Residence',
    category: 'Client',
    col1: [
      'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055344_5eff02e0-87a5-41ce-b64f-eb08da8f33db.png&w=1280&q=85',
      'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055431_11d841fd-8b41-46a5-82e4-b04f2407a7d8.png&w=1280&q=85',
    ],
    col2: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055451_e317bf2d-28d4-48cc-86b0-6f72f25b6327.png&w=1280&q=85',
  },
  {
    number: '02',
    name: "Ado Hall of Worship",
    category: 'Client',
    col1: [
      'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055654_911201c5-36d9-4bc6-bac7-331adfce159f.png&w=1280&q=85',
      'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055723_5ceda0b8-d9c2-4665-b2e3-83ba19ba76d1.png&w=1280&q=85',
    ],
    col2: 'https://images.higgs.ai/?default=1&output=webp&url=https%3A%2F%2Fd8j0ntlcm91z4.cloudfront.net%2Fuser_38xzZboKViGWJOttwIXH07lWA1P%2Fhf_20260412_055753_adc5dcbd-a8e6-49c0-b43a-9b030d835cea.png&w=1280&q=85',
  },
]

// ---------- FadeIn (IntersectionObserver) ----------

function initFadeIn() {
  const elements = document.querySelectorAll('[data-fade]')

  elements.forEach((el) => {
    const x = parseFloat(el.dataset.x || '0')
    const y = parseFloat(el.dataset.y || '30')
    el.style.transform = `translate(${x}px, ${y}px)`
  })

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const el = entry.target
          const delay = parseFloat(el.dataset.delay || '0')
          const duration = parseFloat(el.dataset.duration || '0.7')
          el.style.transitionDelay = `${delay}s`
          el.style.transitionDuration = `${duration}s`
          el.classList.add('is-visible')
          observer.unobserve(el)
        }
      })
    },
    { rootMargin: '50px', threshold: 0 }
  )

  elements.forEach((el) => observer.observe(el))
}

// ---------- Magnet ----------

function initMagnet() {
  const magnets = document.querySelectorAll('[data-magnet]')
  if (!magnets.length) return

  const items = Array.from(magnets).map((el) => ({
    el,
    padding: parseFloat(el.dataset.padding || '150'),
    strength: parseFloat(el.dataset.strength || '3'),
  }))

  window.addEventListener(
    'mousemove',
    (e) => {
      items.forEach(({ el, padding, strength }) => {
        const rect = el.getBoundingClientRect()
        const centerX = rect.left + rect.width / 2
        const centerY = rect.top + rect.height / 2

        const distX = Math.abs(e.clientX - centerX) - rect.width / 2
        const distY = Math.abs(e.clientY - centerY) - rect.height / 2
        const distance = Math.max(distX, distY)

        if (distance < padding) {
          const offsetX = (e.clientX - centerX) / strength
          const offsetY = (e.clientY - centerY) / strength
          el.style.transition = 'transform 0.3s ease-out'
          el.style.transform = `translate3d(${offsetX}px, ${offsetY}px, 0px)`
        } else {
          el.style.transition = 'transform 0.6s ease-in-out'
          el.style.transform = 'translate3d(0px, 0px, 0px)'
        }
      })
    },
    { passive: true }
  )
}

// ---------- Marquee ----------

function buildMarquee() {
  const row1El = document.getElementById('marquee-row-1')
  const row2El = document.getElementById('marquee-row-2')

  const tripled1 = [...marqueeRow1, ...marqueeRow1, ...marqueeRow1]
  const tripled2 = [...marqueeRow2, ...marqueeRow2, ...marqueeRow2]

  tripled1.forEach((src) => {
    const img = document.createElement('img')
    img.src = src
    img.alt = ''
    img.loading = 'lazy'
    row1El.appendChild(img)
  })

  tripled2.forEach((src) => {
    const img = document.createElement('img')
    img.src = src
    img.alt = ''
    img.loading = 'lazy'
    row2El.appendChild(img)
  })
}

function initMarqueeScroll() {
  const section = document.getElementById('marquee')
  const row1El = document.getElementById('marquee-row-1')
  const row2El = document.getElementById('marquee-row-2')

  function handleScroll() {
    const rect = section.getBoundingClientRect()
    const sectionTop = rect.top + window.scrollY
    const offset = (window.scrollY - sectionTop + window.innerHeight) * 0.3

    row1El.style.transform = `translateX(${offset - 200}px)`
    row2El.style.transform = `translateX(${-(offset - 200)}px)`
  }

  handleScroll()
  window.addEventListener('scroll', handleScroll, { passive: true })
}

// ---------- Animated scroll-reveal text ----------

function initAnimatedText() {
  const p = document.getElementById('about-text')
  const text = p.dataset.text
  const characters = text.split('')

  const spans = characters.map((char) => {
    const wrapper = document.createElement('span')
    const ghost = document.createElement('span')
    ghost.className = 'char-ghost'
    ghost.textContent = char
    const anim = document.createElement('span')
    anim.className = 'char-anim'
    anim.textContent = char
    wrapper.appendChild(ghost)
    wrapper.appendChild(anim)
    p.appendChild(wrapper)
    return anim
  })

  function handleScroll() {
    const rect = p.getBoundingClientRect()
    const vh = window.innerHeight
    // progress 0 when paragraph top is at 0.8*vh, progress 1 when bottom is at 0.2*vh
    const start = vh * 0.8
    const end = vh * 0.2
    const total = start - end
    const elapsed = start - rect.top
    let progress = elapsed / (total + rect.height)
    progress = Math.max(0, Math.min(1, progress))

    spans.forEach((span, i) => {
      const charStart = i / spans.length
      const charEnd = charStart + 1 / spans.length
      let charProgress = (progress - charStart) / (charEnd - charStart)
      charProgress = Math.max(0, Math.min(1, charProgress))
      const opacity = 0.2 + charProgress * 0.8
      span.style.opacity = opacity
    })
  }

  handleScroll()
  window.addEventListener('scroll', handleScroll, { passive: true })
}

// ---------- Projects: build cards + sticky stacking scale ----------

function buildProjects() {
  const list = document.getElementById('projects-list')

  projects.forEach((project) => {
    const outer = document.createElement('div')
    outer.className = 'project-card-outer'

    const card = document.createElement('div')
    card.className = 'project-card'

    card.innerHTML = `
      <div class="project-card__top">
        <div class="project-card__info">
          <span class="project-card__number">${project.number}</span>
          <div class="project-card__meta">
            <span class="project-card__category">${project.category}</span>
            <span class="project-card__name">${project.name}</span>
          </div>
        </div>
        <button type="button" class="btn btn--ghost">Live Project</button>
      </div>
      <div class="project-card__images">
        <div class="project-card__col1">
          <img src="${project.col1[0]}" alt="${project.name} detail 1" loading="lazy" />
          <img src="${project.col1[1]}" alt="${project.name} detail 2" loading="lazy" />
        </div>
        <div class="project-card__col2">
          <img src="${project.col2}" alt="${project.name} hero" loading="lazy" />
        </div>
      </div>
    `

    outer.appendChild(card)
    list.appendChild(outer)
  })
}

function initProjectStacking() {
  const outers = Array.from(document.querySelectorAll('.project-card-outer'))
  const total = outers.length

  outers.forEach((outer, index) => {
    outer.style.top = `${96 + index * 28}px`
    const card = outer.querySelector('.project-card')
    const targetScale = 1 - (total - 1 - index) * 0.03

    function handleScroll() {
      const rect = outer.getBoundingClientRect()
      const vh = window.innerHeight
      // progress 0 when card top is at bottom of viewport, 1 when card top reaches top of viewport
      let progress = (vh - rect.top) / vh
      progress = Math.max(0, Math.min(1, progress))
      const scale = 1 + (targetScale - 1) * progress
      card.style.transform = `scale(${scale})`
    }

    handleScroll()
    window.addEventListener('scroll', handleScroll, { passive: true })
  })
}

// ---------- Init ----------

document.addEventListener('DOMContentLoaded', () => {
  initFadeIn()
  initMagnet()
  buildMarquee()
  initMarqueeScroll()
  initAnimatedText()
  buildProjects()
  initProjectStacking()
})
