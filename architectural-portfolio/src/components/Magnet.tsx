import { useRef, useState, useEffect, type ReactNode } from 'react'

interface MagnetProps {
  children: ReactNode
  padding?: number
  strength?: number
  activeTransition?: string
  inactiveTransition?: string
  className?: string
}

export default function Magnet({
  children,
  padding = 150,
  strength = 3,
  activeTransition = 'transform 0.3s ease-out',
  inactiveTransition = 'transform 0.6s ease-in-out',
  className,
}: MagnetProps) {
  const ref = useRef<HTMLDivElement>(null)
  const [transform, setTransform] = useState('translate3d(0px, 0px, 0px)')
  const [transition, setTransition] = useState(inactiveTransition)

  useEffect(() => {
    const handleMouseMove = (e: MouseEvent) => {
      const el = ref.current
      if (!el) return

      const rect = el.getBoundingClientRect()
      const centerX = rect.left + rect.width / 2
      const centerY = rect.top + rect.height / 2

      const distX = Math.abs(e.clientX - centerX) - rect.width / 2
      const distY = Math.abs(e.clientY - centerY) - rect.height / 2
      const distance = Math.max(distX, distY)

      if (distance < padding) {
        const offsetX = (e.clientX - centerX) / strength
        const offsetY = (e.clientY - centerY) / strength
        setTransition(activeTransition)
        setTransform(`translate3d(${offsetX}px, ${offsetY}px, 0px)`)
      } else {
        setTransition(inactiveTransition)
        setTransform('translate3d(0px, 0px, 0px)')
      }
    }

    window.addEventListener('mousemove', handleMouseMove, { passive: true })
    return () => window.removeEventListener('mousemove', handleMouseMove)
  }, [padding, strength, activeTransition, inactiveTransition])

  return (
    <div
      ref={ref}
      className={className}
      style={{
        transform,
        transition,
        willChange: 'transform',
      }}
    >
      {children}
    </div>
  )
}
