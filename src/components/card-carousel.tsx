import { useEffect, useRef, useState } from 'react'
import { TarotCard } from '@/components/tarot-card'
import { useI18n } from '@/lib/i18n'
import { TAROT_CARDS } from '@/lib/tarot-cards'

const VISIBLE_CARD_COUNT = 12
const CAROUSEL_DURATION_MS = 28000
const CARD_W = 88
const CARD_H = CARD_W * 1.5
const RADIUS = 265

function randomCardIds() {
  const ids = TAROT_CARDS.map((card) => card.id)
  for (let i = ids.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[ids[i], ids[j]] = [ids[j], ids[i]]
  }
  return ids.slice(0, VISIBLE_CARD_COUNT)
}

function randomReplacementId(currentIds: number[]) {
  const current = new Set(currentIds)
  const candidates = TAROT_CARDS.filter((card) => !current.has(card.id))
  const pool = candidates.length > 0 ? candidates : TAROT_CARDS
  return pool[Math.floor(Math.random() * pool.length)].id
}

export function CardCarousel() {
  const { t } = useI18n()
  const [cards, setCards] = useState(() => randomCardIds())
  const step = 360 / VISIBLE_CARD_COUNT
  const startedAtRef = useRef(Date.now())
  const pausedRef = useRef(false)
  const pausedAtRef = useRef(0)
  const pausedTotalRef = useRef(0)

  useEffect(() => {
    const swapInterval = CAROUSEL_DURATION_MS / VISIBLE_CARD_COUNT
    const interval = window.setInterval(() => {
      if (pausedRef.current) return

      const elapsed =
        (Date.now() - startedAtRef.current - pausedTotalRef.current) %
        CAROUSEL_DURATION_MS
      const progressAngle = (elapsed / CAROUSEL_DURATION_MS) * 360
      const backSlot =
        Math.round(((180 - progressAngle + 360) % 360) / step) %
        VISIBLE_CARD_COUNT

      setCards((current) => {
        const next = [...current]
        next[backSlot] = randomReplacementId(current)
        return next
      })
    }, swapInterval)

    return () => window.clearInterval(interval)
  }, [step])

  function pauseSwapping() {
    pausedRef.current = true
    pausedAtRef.current = Date.now()
  }

  function resumeSwapping() {
    if (!pausedRef.current) return
    pausedRef.current = false
    pausedTotalRef.current += Date.now() - pausedAtRef.current
  }

  return (
    <div
      className="relative mx-auto h-80 w-full select-none sm:h-96"
      style={{ perspective: '1300px', perspectiveOrigin: '50% 45%' }}
      aria-label={t('carouselAria')}
      onMouseEnter={pauseSwapping}
      onMouseLeave={resumeSwapping}
    >
      <div
        className="carousel-spin absolute left-1/2 top-1/2"
        style={{ transformStyle: 'preserve-3d', height: 0, width: 0 }}
      >
        {cards.map((cardId, i) => {
          const angle = i * step
          return (
            <div
              key={i}
              className="group absolute hover:z-50"
              style={{
                width: CARD_W,
                height: CARD_H,
                left: -CARD_W / 2,
                top: -CARD_H / 2,
                transformStyle: 'preserve-3d',
                transform: `rotateY(${angle}deg) translateZ(${RADIUS}px)`,
              }}
            >
              <div
                className="absolute inset-0"
                style={{ backfaceVisibility: 'hidden' }}
              >
                <div className="h-full w-full transition-transform duration-200 ease-out group-hover:scale-[1.9]">
                  <TarotCard cardId={cardId} faceUp />
                </div>
              </div>
              <div
                className="absolute inset-0"
                style={{
                  backfaceVisibility: 'hidden',
                  transform: 'rotateY(180deg)',
                }}
              >
                <div className="h-full w-full transition-transform duration-200 ease-out group-hover:scale-[1.9]">
                  <TarotCard />
                </div>
              </div>
            </div>
          )
        })}
      </div>
    </div>
  )
}
