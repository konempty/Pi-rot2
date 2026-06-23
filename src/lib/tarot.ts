import { getTarotCard, TAROT_CARDS, TOTAL_CARDS } from '@/lib/tarot-cards'
import {
  getCategoryCopy,
  keyword,
  localizeCardName,
  positionLabels as localizedPositionLabels,
  type Language,
} from '@/lib/i18n'

export { TOTAL_CARDS }

export type CategoryId = 'today' | 'love' | 'money' | 'career' | 'overall'

export type TarotCategory = {
  id: CategoryId
  count: number
  price: number
  icon: string
}

export const CATEGORIES: TarotCategory[] = [
  {
    id: 'today',
    count: 1,
    price: 1,
    icon: 'sun',
  },
  {
    id: 'love',
    count: 3,
    price: 3,
    icon: 'heart',
  },
  {
    id: 'money',
    count: 3,
    price: 3,
    icon: 'coins',
  },
  {
    id: 'career',
    count: 3,
    price: 4,
    icon: 'briefcase',
  },
  {
    id: 'overall',
    count: 5,
    price: 7,
    icon: 'sparkles',
  },
]

export function getCategory(id: CategoryId | null | undefined) {
  return CATEGORIES.find((c) => c.id === id)
}

export function positionLabels(count: number): string[] {
  return localizedPositionLabels('en', count)
}

export type ReadingCard = {
  id: number
  position: string
  keyword: string
  name: string
  kr: string
  text: string
}

export type Reading = {
  summary: string
  cards: ReadingCard[]
  advice: string
}

const KEYWORDS = [
  '새로운 시작',
  '기다림의 미학',
  '용기와 결단',
  '내면의 목소리',
  '풍요로운 결실',
  '관계의 전환',
  '균형 잡기',
  '숨겨진 기회',
  '치유와 회복',
  '직관의 신호',
  '인내의 보상',
  '변화의 바람',
]

function pick<T>(arr: T[], seed: number): T {
  return arr[Math.abs(seed) % arr.length]
}

export function shuffledDeck() {
  const deck = TAROT_CARDS.map((card) => card.id)
  for (let i = deck.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1))
    ;[deck[i], deck[j]] = [deck[j], deck[i]]
  }
  return deck
}

export function generateMockReading(
  categoryId: CategoryId,
  cardIds: number[],
  language: Language,
  t: (key: string, params?: Record<string, string | number>) => string,
): Reading {
  const category = getCategory(categoryId)
  const categoryCopy = getCategoryCopy(language, categoryId)
  const labels = localizedPositionLabels(language, cardIds.length)

  const cards: ReadingCard[] = cardIds.map((id, i) => {
    const card = getTarotCard(id)
    const keywordIndex = Math.abs(id + i) % KEYWORDS.length
    const pickedKeyword = keyword(language, keywordIndex)
    const name = localizeCardName(card, language) || `Card ${id}`
    const kr = language === 'ko' ? card?.kr ?? '' : ''
    const position = labels[i] ?? t('positionNth', { n: i + 1 })
    return {
      id,
      position,
      keyword: pickedKeyword,
      name,
      kr,
      text: t('readingText', {
        card: name,
        keyword: pickedKeyword,
        position,
      }),
    }
  })

  return {
    summary: t('summary', {
      category: categoryCopy?.name ?? category?.id ?? 'Tarot',
    }),
    cards,
    advice: t('advice'),
  }
}
