import { cn } from '@/lib/utils'
import { publicAsset } from '@/lib/asset-path'

export function PiCoin({
  size = 24,
  className,
}: {
  size?: number
  className?: string
}) {
  return (
    <img
      src={publicAsset('pi-coin.png')}
      alt="파이코인"
      width={size}
      height={size}
      className={cn('inline-block rounded-full', className)}
    />
  )
}

export function Wordmark({ className }: { className?: string }) {
  return (
    <span className={cn('inline-flex items-baseline gap-1.5', className)}>
      <span className="font-serif text-2xl font-semibold tracking-tight text-primary text-glow-gold">
        PI
      </span>
      <span className="font-serif text-2xl font-semibold tracking-tight text-foreground">
        -rot
      </span>
    </span>
  )
}
