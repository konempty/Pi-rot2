import { useEffect, useMemo, useRef, useState } from 'react'
import {
  ArrowRight,
  Briefcase,
  Check,
  ChevronRight,
  Coins,
  Heart,
  Home,
  Loader2,
  Moon,
  MousePointerClick,
  Quote,
  RotateCcw,
  ShieldCheck,
  Sparkles,
  Star,
  Sun,
  WandSparkles,
  type LucideIcon,
} from 'lucide-react'
import { Button } from '@/components/ui/button'
import { CardCarousel } from '@/components/card-carousel'
import { useFlow } from '@/components/flow-provider'
import { LanguageSelector } from '@/components/language-selector'
import { LanguageWelcomeModal } from '@/components/language-welcome-modal'
import { PiCoin, Wordmark } from '@/components/pi-logo'
import { StepHeader } from '@/components/step-header'
import { TarotCard } from '@/components/tarot-card'
import { getCategoryCopy, useI18n } from '@/lib/i18n'
import {
  CATEGORIES,
  generateMockReading,
  getCategory,
  shuffledDeck,
  TOTAL_CARDS,
  type CategoryId,
} from '@/lib/tarot'

type Route = '/' | '/categories' | '/payment' | '/select' | '/loading' | '/result'

const ROUTES = new Set<Route>([
  '/',
  '/categories',
  '/payment',
  '/select',
  '/loading',
  '/result',
])

const STEP_ICONS = [Sparkles, MousePointerClick, WandSparkles]

const ICONS: Record<string, LucideIcon> = {
  sun: Sun,
  heart: Heart,
  coins: Coins,
  briefcase: Briefcase,
  sparkles: Sparkles,
}

const LOADING_MESSAGE_KEYS = ['loading1', 'loading2', 'loading3', 'loading4']

const MOCK_BALANCE = 128.5
const BASE_PATH = import.meta.env.BASE_URL.replace(/\/$/, '')

function stripBasePath(pathname: string) {
  if (!BASE_PATH || BASE_PATH === '') return pathname
  if (!pathname.startsWith(BASE_PATH)) return pathname
  return pathname.slice(BASE_PATH.length) || '/'
}

function withBasePath(route: Route) {
  if (!BASE_PATH || BASE_PATH === '') return route
  return `${BASE_PATH}${route === '/' ? '/' : route}`
}

function currentRoute(): Route {
  const path = stripBasePath(window.location.pathname) as Route
  return ROUTES.has(path) ? path : '/'
}

export function App() {
  const [route, setRoute] = useState<Route>(() => currentRoute())

  function navigate(path: string) {
    const next = (ROUTES.has(path as Route) ? path : '/') as Route
    history.pushState(null, '', withBasePath(next))
    setRoute(next)
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }

  useEffect(() => {
    const onPop = () => setRoute(currentRoute())
    window.addEventListener('popstate', onPop)
    return () => window.removeEventListener('popstate', onPop)
  }, [])

  let page = <HomePage navigate={navigate} />
  if (route === '/categories') page = <CategoriesPage navigate={navigate} />
  if (route === '/payment') page = <PaymentPage navigate={navigate} />
  if (route === '/select') page = <SelectPage navigate={navigate} />
  if (route === '/loading') page = <LoadingPage navigate={navigate} />
  if (route === '/result') page = <ResultPage navigate={navigate} />

  return (
    <>
      {page}
      <LanguageWelcomeModal />
    </>
  )
}

function HomePage({ navigate }: { navigate: (path: string) => void }) {
  const { t } = useI18n()

  return (
    <main className="relative min-h-dvh overflow-hidden bg-starfield">
      <header className="mx-auto flex w-full max-w-7xl items-center justify-between px-5 py-5 sm:px-8">
        <Wordmark />
        <div className="flex items-center gap-2">
          <span className="hidden items-center gap-1.5 rounded-full border border-primary/30 bg-card/60 px-3 py-1.5 text-xs font-medium text-primary sm:inline-flex">
            <PiCoin size={16} />
            {t('piPayment')}
          </span>
          <LanguageSelector />
        </div>
      </header>

      <section className="mx-auto flex w-full max-w-4xl flex-col items-center px-5 pt-6 text-center sm:px-8">
        <span className="mb-5 inline-flex items-center gap-1.5 rounded-full border border-border bg-card/50 px-3 py-1 text-xs text-muted-foreground">
          <Sparkles className="size-3.5 text-primary" />
          {t('heroBadge')}
        </span>
        <h1 className="text-balance font-serif text-5xl font-bold leading-tight text-foreground sm:text-6xl">
          {t('heroLine1')}
          <br />
          <span className="text-primary text-glow-gold">{t('heroLine2')}</span>
        </h1>
        <p className="mt-5 max-w-md text-pretty leading-relaxed text-muted-foreground">
          {t('heroBody')}
        </p>

        <div className="mt-8 flex flex-col items-center gap-3 sm:flex-row">
          <Button
            size="lg"
            className="h-12 gap-2 rounded-full px-7 text-base font-semibold"
            onClick={() => navigate('/categories')}
          >
            {t('startReading')}
            <ArrowRight className="size-4" />
          </Button>
          <span className="text-xs text-muted-foreground">
            {t('priceHint')}
          </span>
        </div>
      </section>

      <section className="mx-auto mt-14 w-full max-w-6xl px-5 sm:px-8">
        <CardCarousel />
        <p className="mt-4 text-center text-xs text-muted-foreground">
          {t('carouselCaption')}
        </p>
      </section>

      <section className="mx-auto mt-16 w-full max-w-6xl px-5 pb-20 sm:px-8">
        <h2 className="mb-8 text-center font-serif text-2xl font-semibold text-foreground">
          {t('howItWorks')}
        </h2>
        <ol className="grid gap-4 sm:grid-cols-3">
          {STEP_ICONS.map((Icon, i) => (
            <li
              key={i}
              className="rounded-2xl border border-border bg-card/50 p-5"
            >
              <div className="mb-4 flex items-center justify-between">
                <span className="flex size-10 items-center justify-center rounded-full bg-primary/15 text-primary">
                  <Icon className="size-5" />
                </span>
                <span className="font-serif text-3xl font-bold text-primary/30">
                  {i + 1}
                </span>
              </div>
              <h3 className="mb-1.5 font-medium text-foreground">
                {t(`step${i + 1}Title`)}
              </h3>
              <p className="text-sm leading-relaxed text-muted-foreground">
                {t(`step${i + 1}Desc`)}
              </p>
            </li>
          ))}
        </ol>
      </section>

      <footer className="border-t border-border/60 py-6 text-center text-xs text-muted-foreground">
        <PiCoin size={14} className="mr-1.5 align-middle" />
        {t('footer')}
      </footer>
    </main>
  )
}

function CategoriesPage({ navigate }: { navigate: (path: string) => void }) {
  const { setCategory } = useFlow()
  const { language, t } = useI18n()

  function choose(id: CategoryId) {
    setCategory(id)
    navigate('/payment')
  }

  return (
    <main className="min-h-dvh bg-starfield">
      <StepHeader step={1} backHref="/" navigate={navigate} />
      <div className="mx-auto w-full max-w-5xl px-5 pb-20 pt-8 sm:px-8">
        <h1 className="text-balance font-serif text-3xl font-bold text-foreground sm:text-4xl">
          {t('categoriesTitle')}
        </h1>
        <p className="mt-2 text-pretty leading-relaxed text-muted-foreground">
          {t('categoriesDesc')}
        </p>

        <ul className="mt-7 grid gap-3 md:grid-cols-2">
          {CATEGORIES.map((c) => {
            const Icon = ICONS[c.icon] ?? Sparkles
            const categoryCopy = getCategoryCopy(language, c.id)
            return (
              <li key={c.id}>
                <button
                  type="button"
                  onClick={() => choose(c.id)}
                  className="group flex w-full items-center gap-4 rounded-2xl border border-border bg-card/50 p-4 text-left transition-all hover:border-primary/50 hover:bg-card"
                >
                  <span className="flex size-12 shrink-0 items-center justify-center rounded-xl bg-primary/15 text-primary">
                    <Icon className="size-6" />
                  </span>
                  <span className="min-w-0 flex-1">
                    <span className="flex items-center gap-2">
                      <span className="font-medium text-foreground">
                        {categoryCopy?.name}
                      </span>
                      <span className="rounded-full bg-secondary px-2 py-0.5 text-[11px] text-secondary-foreground">
                        {c.count}
                        {t('cardsUnit')}
                      </span>
                    </span>
                    <span className="mt-0.5 block truncate text-sm text-muted-foreground">
                      {categoryCopy?.tagline}
                    </span>
                  </span>
                  <span className="flex shrink-0 items-center gap-1 font-serif text-lg font-semibold text-primary">
                    <PiCoin size={18} />
                    {c.price}
                  </span>
                  <ChevronRight className="size-5 shrink-0 text-muted-foreground transition-transform group-hover:translate-x-0.5 group-hover:text-primary" />
                </button>
              </li>
            )
          })}
        </ul>
      </div>
    </main>
  )
}

function PaymentPage({ navigate }: { navigate: (path: string) => void }) {
  const { categoryId, setPaid } = useFlow()
  const { language, t } = useI18n()
  const [status, setStatus] = useState<'idle' | 'processing' | 'done'>('idle')
  const category = getCategory(categoryId)
  const categoryCopy = getCategoryCopy(language, categoryId)

  useEffect(() => {
    if (!categoryId) navigate('/categories')
  }, [categoryId, navigate])

  function pay() {
    setStatus('processing')
    setTimeout(() => {
      setStatus('done')
      setPaid(true)
      setTimeout(() => navigate('/select'), 750)
    }, 1600)
  }

  if (!category) return null
  const total = category.price

  return (
    <main className="min-h-dvh bg-starfield">
      <StepHeader step={2} backHref="/categories" navigate={navigate} />
      <div className="mx-auto w-full max-w-xl px-5 pb-28 pt-8 sm:px-8">
        <h1 className="font-serif text-3xl font-bold text-foreground">
          {t('paymentTitle')}
        </h1>
        <p className="mt-2 text-sm text-muted-foreground">
          {t('paymentDesc')}
        </p>

        <div className="mt-7 rounded-2xl border border-border bg-card/60 p-5">
          <div className="flex items-center justify-between">
            <span className="text-muted-foreground">{t('paymentTopic')}</span>
            <span className="font-medium text-foreground">{categoryCopy?.name}</span>
          </div>
          <div className="mt-3 flex items-center justify-between">
            <span className="text-muted-foreground">{t('paymentCardCount')}</span>
            <span className="font-medium text-foreground">
              {category.count}
              {t('cardsUnit')}
            </span>
          </div>
          <div className="mt-3 flex items-center justify-between">
            <span className="text-muted-foreground">{t('paymentNetworkFee')}</span>
            <span className="font-medium text-foreground">0 π</span>
          </div>
          <div className="my-4 border-t border-border/60" />
          <div className="flex items-center justify-between">
            <span className="font-medium text-foreground">{t('paymentTotal')}</span>
            <span className="flex items-center gap-1.5 font-serif text-2xl font-bold text-primary">
              <PiCoin size={22} />
              {total} π
            </span>
          </div>
        </div>

        <div className="mt-4 flex items-center justify-between rounded-2xl border border-border bg-card/40 px-5 py-4">
          <span className="flex items-center gap-2.5">
            <PiCoin size={28} />
            <span>
              <span className="block text-sm font-medium text-foreground">
                {t('wallet')}
              </span>
              <span className="block text-xs text-muted-foreground">
                {t('balance')} {MOCK_BALANCE} π
              </span>
            </span>
          </span>
          <span className="rounded-full bg-primary/15 px-2.5 py-1 text-xs font-medium text-primary">
            {t('connected')}
          </span>
        </div>

        <p className="mt-4 flex items-center justify-center gap-1.5 text-xs text-muted-foreground">
          <ShieldCheck className="size-3.5 text-primary" />
          {t('paymentSafety')}
        </p>
      </div>

      <div className="fixed inset-x-0 bottom-0 border-t border-border/60 bg-background/90 backdrop-blur">
        <div className="mx-auto w-full max-w-xl px-5 py-4 sm:px-8">
          <Button
            size="lg"
            disabled={status !== 'idle'}
            onClick={pay}
            className="h-12 w-full gap-2 rounded-full text-base font-semibold"
          >
            {status === 'idle' && (
              <>
                <PiCoin size={20} />
                {t('payButton', { amount: total })}
              </>
            )}
            {status === 'processing' && (
              <>
                <Loader2 className="size-5 animate-spin" />
                {t('paymentProcessing')}
              </>
            )}
            {status === 'done' && (
              <>
                <Check className="size-5" />
                {t('paymentDone')}
              </>
            )}
          </Button>
        </div>
      </div>
    </main>
  )
}

function SelectPage({ navigate }: { navigate: (path: string) => void }) {
  const { categoryId, paid, setSelectedCards } = useFlow()
  const { t } = useI18n()
  const category = getCategory(categoryId)
  const count = category?.count ?? 0
  const fanScrollRef = useRef<HTMLDivElement | null>(null)
  const [deck, setDeck] = useState<number[]>([])
  const [picked, setPicked] = useState<number[]>([])
  const [fanScroll, setFanScroll] = useState({ left: 0, width: 100 })

  useEffect(() => {
    if (!categoryId || !paid) {
      navigate('/categories')
      return
    }
    setDeck(shuffledDeck())
  }, [categoryId, paid, navigate])

  const isFull = picked.length === count
  const remaining = useMemo(() => count - picked.length, [count, picked.length])
  const fanWidth = Math.max(1800, deck.length * 26 + 320)
  const fanStep = deck.length > 1 ? (fanWidth - 260) / (deck.length - 1) : 0
  const fanMid = Math.max(1, (deck.length - 1) / 2)

  function syncFanScroll() {
    const el = fanScrollRef.current
    if (!el) return

    const maxScroll = el.scrollWidth - el.clientWidth
    if (maxScroll <= 0) {
      setFanScroll({ left: 0, width: 100 })
      return
    }

    const width = Math.max(18, (el.clientWidth / el.scrollWidth) * 100)
    const left = (el.scrollLeft / maxScroll) * (100 - width)
    setFanScroll({ left, width })
  }

  useEffect(() => {
    const el = fanScrollRef.current
    if (!el || deck.length === 0) return
    requestAnimationFrame(() => {
      el.scrollLeft = (el.scrollWidth - el.clientWidth) / 2
      syncFanScroll()
    })
  }, [deck.length])

  useEffect(() => {
    syncFanScroll()
    window.addEventListener('resize', syncFanScroll)
    return () => window.removeEventListener('resize', syncFanScroll)
  }, [deck.length])

  function toggle(pos: number) {
    setPicked((prev) => {
      if (prev.includes(pos)) return prev.filter((p) => p !== pos)
      if (prev.length >= count) return prev
      return [...prev, pos]
    })
  }

  function confirm() {
    setSelectedCards(picked.map((pos) => deck[pos]))
    navigate('/loading')
  }

  if (!category) return null

  return (
    <main className="min-h-dvh bg-starfield">
      <StepHeader step={3} backHref="/payment" navigate={navigate} />
      <div className="mx-auto w-full px-5 pb-32 pt-7 sm:px-8">
        <div className="text-center">
          <h1 className="font-serif text-3xl font-bold text-foreground">
            {t('selectTitle')}
          </h1>
          <p className="mt-2 text-pretty leading-relaxed text-muted-foreground">
            {t('selectDescPrefix')}
            <strong className="text-primary">
              {count}
              {t('cardsUnit')}
            </strong>
            {t('selectDescSuffix')}
          </p>
          <p className="mt-3 inline-flex items-center gap-1.5 rounded-full border border-primary/30 bg-card/60 px-3 py-1 text-sm font-medium text-primary">
            <Sparkles className="size-4" />
            {isFull ? t('selectionComplete') : t('remainingCards', { count: remaining })}
          </p>
        </div>

        <div className="mt-5 flex items-center justify-center gap-3 text-xs font-medium text-primary/85">
          <span aria-hidden="true">←</span>
          <span>{t('scrollSpreadHint')}</span>
          <span aria-hidden="true">→</span>
        </div>

        <div className="relative left-1/2 mt-3 w-screen -translate-x-1/2">
          <div
            className="pointer-events-none absolute inset-y-8 left-0 z-40 w-px bg-primary/45 shadow-[0_0_14px_oklch(0.82_0.13_80_/_45%)]"
            aria-hidden="true"
          />
          <div
            className="pointer-events-none absolute inset-y-8 right-0 z-40 w-px bg-primary/45 shadow-[0_0_14px_oklch(0.82_0.13_80_/_45%)]"
            aria-hidden="true"
          />
          <div
            ref={fanScrollRef}
            onScroll={syncFanScroll}
            className="scrollbar-none overflow-x-auto overflow-y-hidden px-5 pb-10 pt-8 sm:px-8"
          >
          <div
            className="relative mx-auto h-[330px] sm:h-[420px]"
            style={{ width: fanWidth }}
          >
          {deck.map((cardId, pos) => {
            const order = picked.indexOf(pos)
            const selected = order !== -1
            const dim = isFull && !selected
            const offset = (pos - fanMid) / fanMid
            const angle = offset * 36
            const curve = 34 + Math.pow(Math.abs(offset), 1.72) * 142
            const left = 110 + pos * fanStep
            return (
              <button
                key={`${cardId}-${pos}`}
                type="button"
                onClick={() => toggle(pos)}
                aria-pressed={selected}
                aria-label={t('selectCardAria', { n: pos + 1 })}
                className="absolute origin-bottom rounded-xl transition-opacity duration-200 hover:z-50 focus-visible:z-50"
                style={{
                  left,
                  top: curve,
                  zIndex: selected ? 80 : pos,
                  transform: `translateX(-50%) rotate(${angle}deg)`,
                }}
              >
                <div
                  className={
                    'w-[70px] transition-transform duration-200 ease-out sm:w-[82px] ' +
                    (selected
                      ? '-translate-y-10 scale-110'
                      : 'hover:-translate-y-8 hover:scale-105 focus-visible:-translate-y-8 focus-visible:scale-105') +
                    (dim ? ' opacity-35' : '')
                  }
                >
                  <div className="relative">
                    <TarotCard selected={selected} />
                    {selected && (
                      <span
                        className="absolute -right-2 -top-2 z-10 flex size-6 items-center justify-center rounded-full bg-primary font-serif text-xs font-bold text-primary-foreground shadow sm:-right-2.5 sm:-top-2.5 sm:size-7 sm:text-sm"
                        style={{ transform: `rotate(${-angle}deg)` }}
                      >
                        {order + 1}
                      </span>
                    )}
                  </div>
                </div>
              </button>
            )
          })}
            </div>
          </div>
        </div>
        <div
          className="relative mx-auto mt-1 h-1.5 w-44 overflow-hidden rounded-full bg-primary/15"
          aria-hidden="true"
        >
          <div
            className="absolute inset-y-0 rounded-full bg-primary/75 shadow-[0_0_10px_oklch(0.82_0.13_80_/_35%)]"
            style={{
              left: `${fanScroll.left}%`,
              width: `${fanScroll.width}%`,
            }}
          />
        </div>
      </div>

      <div className="fixed inset-x-0 bottom-0 border-t border-border/60 bg-background/90 backdrop-blur">
        <div className="mx-auto w-full max-w-4xl px-5 py-4 sm:px-8">
          <Button
            size="lg"
            disabled={!isFull}
            onClick={confirm}
            className="h-12 w-full gap-2 rounded-full text-base font-semibold"
          >
            {isFull ? t('confirmResult') : t('confirmRemaining', { count: remaining })}
          </Button>
        </div>
      </div>
    </main>
  )
}

function LoadingPage({ navigate }: { navigate: (path: string) => void }) {
  const { categoryId, paid, selectedCards } = useFlow()
  const { t } = useI18n()
  const [msgIndex, setMsgIndex] = useState(0)

  useEffect(() => {
    if (!categoryId || !paid || selectedCards.length === 0) {
      navigate('/categories')
      return
    }

      const interval = setInterval(() => {
      setMsgIndex((i) => (i + 1) % LOADING_MESSAGE_KEYS.length)
    }, 1800)
    const timeout = setTimeout(() => navigate('/result'), 5200)

    return () => {
      clearInterval(interval)
      clearTimeout(timeout)
    }
  }, [categoryId, paid, selectedCards, navigate])

  return (
    <main className="flex min-h-dvh flex-col items-center justify-center bg-starfield px-6 text-center">
      <div className="relative flex size-56 items-center justify-center">
        <div className="absolute inset-0 animate-orbit">
          <Star className="absolute left-1/2 top-0 size-5 -translate-x-1/2 fill-primary text-primary" />
          <Moon className="absolute bottom-2 left-2 size-5 text-primary/70" />
          <Sparkles className="absolute right-2 top-1/3 size-5 text-primary/80" />
        </div>
        <div className="absolute inset-6 rounded-full border border-primary/20" />
        <div className="absolute inset-12 rounded-full border border-primary/15" />
        <div className="relative flex size-24 items-center justify-center rounded-full border border-primary/40 bg-card/60 shadow-lg shadow-primary/20">
          <PiCoin size={56} className="animate-shimmer" />
        </div>
      </div>

      <h1 className="mt-10 font-serif text-2xl font-semibold text-foreground sm:text-3xl">
        {t('loadingTitle')}
      </h1>
      <p
        key={msgIndex}
        className="mt-3 min-h-6 animate-shimmer text-pretty text-muted-foreground"
      >
        {t(LOADING_MESSAGE_KEYS[msgIndex])}
      </p>

      <div className="mt-8 flex items-center gap-1.5" aria-hidden="true">
        {LOADING_MESSAGE_KEYS.map((_, i) => (
          <span
            key={i}
            className={
              'size-2 rounded-full transition-colors ' +
              (i === msgIndex ? 'bg-primary' : 'bg-border')
            }
          />
        ))}
      </div>
    </main>
  )
}

function ResultPage({ navigate }: { navigate: (path: string) => void }) {
  const { categoryId, paid, selectedCards, reset } = useFlow()
  const { language, t } = useI18n()
  const category = getCategory(categoryId)
  const categoryCopy = getCategoryCopy(language, categoryId)

  useEffect(() => {
    if (!categoryId || !paid || selectedCards.length === 0) {
      navigate('/categories')
    }
  }, [categoryId, paid, selectedCards, navigate])

  const reading = useMemo(() => {
    if (!categoryId || selectedCards.length === 0) return null
    return generateMockReading(categoryId, selectedCards, language, t)
  }, [categoryId, language, selectedCards, t])

  function restart() {
    reset()
    navigate('/categories')
  }

  if (!category || !reading) return null

  return (
    <main className="min-h-dvh bg-starfield">
      <StepHeader step={3} total={3} backHref="/" navigate={navigate} />
      <div className="mx-auto w-full max-w-6xl px-5 pb-32 pt-8 sm:px-8">
        <div className="text-center">
          <span className="inline-flex items-center gap-1.5 rounded-full border border-primary/30 bg-card/60 px-3 py-1 text-xs font-medium text-primary">
            <Sparkles className="size-3.5" />
            {t('resultBadge', { category: categoryCopy?.name ?? category.id })}
          </span>
          <h1 className="mt-4 text-balance font-serif text-3xl font-bold text-foreground sm:text-4xl">
            {t('resultTitle')}
          </h1>
        </div>

        <div
          className="mt-8 grid gap-3"
          style={{
            gridTemplateColumns: `repeat(${Math.min(reading.cards.length, 5)}, minmax(0, 1fr))`,
          }}
        >
          {reading.cards.map((card, i) => (
            <div
              key={`${card.id}-${i}`}
              className="relative z-0 flex animate-float-slow flex-col items-center gap-2"
              style={{ animationDelay: `${i * 0.5}s` }}
            >
              <div className="relative z-0 w-full">
                <TarotCard cardId={card.id} faceUp />
              </div>
              <span className="text-center text-[11px] leading-tight text-muted-foreground">
                {card.position}
              </span>
            </div>
          ))}
        </div>

        <section className="mt-8 rounded-2xl border border-primary/30 bg-card/60 p-5">
          <h2 className="mb-2 flex items-center gap-2 font-serif text-lg font-semibold text-primary">
            <Quote className="size-4" />
            {t('summaryTitle')}
          </h2>
          <p className="text-pretty leading-relaxed text-foreground/90">
            {reading.summary}
          </p>
        </section>

        <section className="mt-5 grid gap-4 lg:grid-cols-2">
          {reading.cards.map((card, i) => (
            <div
              key={`${card.id}-${i}-detail`}
              className="flex gap-4 rounded-2xl border border-border bg-card/40 p-4"
            >
              <div className="relative z-0 w-16 shrink-0">
                <TarotCard
                  cardId={card.id}
                  faceUp
                />
              </div>
              <div className="min-w-0">
                <div className="flex flex-wrap items-center gap-2">
                  <span className="font-medium text-foreground">
                    {card.position}
                  </span>
                  <span className="rounded-full bg-primary/15 px-2 py-0.5 text-[11px] text-primary">
                    {card.keyword}
                  </span>
                </div>
                <p className="mt-1 text-xs text-primary/80">
                  {card.name}
                </p>
                <p className="mt-1.5 text-sm leading-relaxed text-muted-foreground">
                  {card.text}
                </p>
              </div>
            </div>
          ))}
        </section>

        <section className="mt-5 rounded-2xl border border-border bg-secondary/40 p-5">
          <h2 className="mb-2 flex items-center gap-2 font-serif text-lg font-semibold text-foreground">
            <Sparkles className="size-4 text-primary" />
            {t('detailAdviceTitle')}
          </h2>
          <p className="text-pretty leading-relaxed text-foreground/90">
            {reading.advice}
          </p>
        </section>
      </div>

      <div className="fixed inset-x-0 bottom-0 border-t border-border/60 bg-background/90 backdrop-blur">
        <div className="mx-auto flex w-full max-w-4xl gap-3 px-5 py-4 sm:px-8">
          <Button
            variant="outline"
            size="lg"
            className="h-12 flex-1 gap-2 rounded-full"
            onClick={() => navigate('/')}
          >
            <Home className="size-4" />
            {t('home')}
          </Button>
          <Button
            size="lg"
            onClick={restart}
            className="h-12 flex-1 gap-2 rounded-full font-semibold"
          >
            <RotateCcw className="size-4" />
            {t('restart')}
          </Button>
        </div>
      </div>
    </main>
  )
}

void TOTAL_CARDS
