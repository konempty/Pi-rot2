import { CARD_BACK_IMAGE, getTarotCard } from '@/lib/tarot-cards'
import { localizeCardName, useI18n } from '@/lib/i18n'
import { cn } from '@/lib/utils'

type TarotCardProps = {
  cardId?: number
  faceUp?: boolean
  selected?: boolean
  className?: string
  imageClassName?: string
}

export function TarotCard({
  cardId,
  faceUp = false,
  selected = false,
  className,
  imageClassName,
}: TarotCardProps) {
  const { language, t } = useI18n()
  const card = typeof cardId === 'number' ? getTarotCard(cardId) : undefined
  const src = faceUp && card ? card.image : CARD_BACK_IMAGE
  const label = faceUp && card ? localizeCardName(card, language) : t('cardBackAlt')

  return (
    <div
      className={cn(
        'relative aspect-[2/3] w-full rounded-xl transition-all duration-300',
        selected
          ? 'shadow-xl shadow-primary/30 ring-2 ring-primary/70'
          : 'shadow-lg shadow-black/20',
        className,
      )}
    >
      <img
        src={src}
        alt={label}
        draggable={false}
        className={cn(
          'h-full w-full select-none object-contain',
          imageClassName,
        )}
      />
    </div>
  )
}
