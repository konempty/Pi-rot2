import { ChevronLeft } from 'lucide-react'
import { LanguageSelector } from '@/components/language-selector'
import { Wordmark } from '@/components/pi-logo'

export function StepHeader({
  step,
  total = 3,
  backHref,
  navigate,
}: {
  step: number
  total?: number
  backHref?: string
  navigate: (path: string) => void
}) {
  return (
    <header className="sticky top-0 z-20 border-b border-border/60 bg-background/80 backdrop-blur">
      <div className="mx-auto flex w-full max-w-7xl items-center justify-between px-5 py-3.5 sm:px-8">
        <button
          type="button"
          onClick={() => (backHref ? navigate(backHref) : history.back())}
          className="flex size-9 items-center justify-center rounded-full border border-border text-muted-foreground transition-colors hover:text-foreground"
          aria-label="뒤로 가기"
        >
          <ChevronLeft className="size-5" />
        </button>
        <Wordmark className="[&_span]:text-lg" />
        <div className="flex items-center gap-2">
          <div className="hidden items-center gap-1.5 sm:flex" aria-hidden="true">
            {Array.from({ length: total }).map((_, i) => (
              <span
                key={i}
                className={
                  'h-1.5 rounded-full transition-all ' +
                  (i + 1 === step
                    ? 'w-5 bg-primary'
                    : i + 1 < step
                      ? 'w-1.5 bg-primary/60'
                      : 'w-1.5 bg-border')
                }
              />
            ))}
          </div>
          <LanguageSelector />
        </div>
      </div>
    </header>
  )
}
