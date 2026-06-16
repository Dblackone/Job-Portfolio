import { useEffect, useRef, useState } from 'react'
import { marqueeRow1, marqueeRow2 } from '../data/marqueeImages'

function tripleImages(images: string[]) {
  return [...images, ...images, ...images]
}

export default function MarqueeSection() {
  const sectionRef = useRef<HTMLDivElement>(null)
  const [offset, setOffset] = useState(0)

  useEffect(() => {
    const handleScroll = () => {
      const section = sectionRef.current
      if (!section) return

      const sectionTop = section.getBoundingClientRect().top + window.scrollY
      const value =
        (window.scrollY - sectionTop + window.innerHeight) * 0.3
      setOffset(value)
    }

    handleScroll()
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const row1Images = tripleImages(marqueeRow1)
  const row2Images = tripleImages(marqueeRow2)

  return (
    <section
      ref={sectionRef}
      className="overflow-hidden pb-10 pt-24 sm:pt-32 md:pt-40"
      style={{ background: '#0C0C0C' }}
    >
      <div
        className="mb-3 flex gap-3"
        style={{
          transform: `translateX(${offset - 200}px)`,
          willChange: 'transform',
        }}
      >
        {row1Images.map((src, i) => (
          <img
            key={`row1-${i}`}
            src={src}
            alt=""
            loading="lazy"
            className="h-[270px] w-[420px] flex-shrink-0 rounded-2xl object-cover"
          />
        ))}
      </div>

      <div
        className="flex gap-3"
        style={{
          transform: `translateX(${-(offset - 200)}px)`,
          willChange: 'transform',
        }}
      >
        {row2Images.map((src, i) => (
          <img
            key={`row2-${i}`}
            src={src}
            alt=""
            loading="lazy"
            className="h-[270px] w-[420px] flex-shrink-0 rounded-2xl object-cover"
          />
        ))}
      </div>
    </section>
  )
}
