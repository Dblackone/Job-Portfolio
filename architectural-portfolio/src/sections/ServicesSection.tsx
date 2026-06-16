import FadeIn from '../components/FadeIn'

const services = [
  {
    number: '01',
    name: 'Architectural Design',
    description:
      'Concept-to-detail design development that translates client vision into buildable, code-compliant architecture.',
  },
  {
    number: '02',
    name: 'BIM Modeling & Coordination',
    description:
      'Revit-based BIM modeling, clash detection, and multi-discipline coordination to keep projects accurate and on schedule.',
  },
  {
    number: '03',
    name: 'Construction Project Management',
    description:
      'On-site and remote project oversight covering scheduling, budgeting, quality control, and stakeholder communication.',
  },
  {
    number: '04',
    name: '3D Visualization & Rendering',
    description:
      'Photorealistic interior and exterior renders that help clients see and approve their space before a single block is laid.',
  },
  {
    number: '05',
    name: 'Interior & Landscape Design',
    description:
      'Space planning, material selection, and landscape concepts that complete a project from structure to finish.',
  },
]

export default function ServicesSection() {
  return (
    <section
      id="price"
      className="rounded-t-[40px] bg-white px-5 py-20 sm:rounded-t-[50px] sm:px-8 sm:py-24 md:rounded-t-[60px] md:px-10 md:py-32"
    >
      <h2
        className="mb-16 text-center font-black uppercase text-[#0C0C0C] sm:mb-20 md:mb-28"
        style={{ fontSize: 'clamp(3rem, 12vw, 160px)' }}
      >
        Services
      </h2>

      <div className="mx-auto max-w-5xl">
        {services.map((service, i) => (
          <FadeIn key={service.number} delay={i * 0.1}>
            <div
              className="flex gap-6 py-8 sm:py-10 md:py-12"
              style={{
                borderBottom:
                  i < services.length - 1
                    ? '1px solid rgba(12, 12, 12, 0.15)'
                    : 'none',
              }}
            >
              <span
                className="flex-shrink-0 font-black text-[#0C0C0C]"
                style={{ fontSize: 'clamp(3rem, 10vw, 140px)' }}
              >
                {service.number}
              </span>
              <div className="flex flex-col gap-3 justify-center">
                <h3
                  className="font-medium uppercase text-[#0C0C0C]"
                  style={{ fontSize: 'clamp(1rem, 2.2vw, 2.1rem)' }}
                >
                  {service.name}
                </h3>
                <p
                  className="max-w-2xl font-light leading-relaxed text-[#0C0C0C] opacity-60"
                  style={{ fontSize: 'clamp(0.85rem, 1.6vw, 1.25rem)' }}
                >
                  {service.description}
                </p>
              </div>
            </div>
          </FadeIn>
        ))}
      </div>
    </section>
  )
}
