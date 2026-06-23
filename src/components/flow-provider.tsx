import {
  createContext,
  useCallback,
  useContext,
  useEffect,
  useState,
  type ReactNode,
} from 'react'
import type { CategoryId } from '@/lib/tarot'

type FlowState = {
  categoryId: CategoryId | null
  paid: boolean
  selectedCards: number[]
}

type FlowContextValue = FlowState & {
  setCategory: (id: CategoryId) => void
  setPaid: (paid: boolean) => void
  setSelectedCards: (cards: number[]) => void
  reset: () => void
}

const STORAGE_KEY = 'pirot-flow'
const initialState: FlowState = {
  categoryId: null,
  paid: false,
  selectedCards: [],
}

const FlowContext = createContext<FlowContextValue | null>(null)

export function FlowProvider({ children }: { children: ReactNode }) {
  const [state, setState] = useState<FlowState>(initialState)

  useEffect(() => {
    try {
      const raw = sessionStorage.getItem(STORAGE_KEY)
      if (raw) setState(JSON.parse(raw))
    } catch {
      // Session storage is optional for this local prototype.
    }
  }, [])

  useEffect(() => {
    try {
      sessionStorage.setItem(STORAGE_KEY, JSON.stringify(state))
    } catch {
      // Ignore private browsing or storage failures.
    }
  }, [state])

  const setCategory = useCallback((id: CategoryId) => {
    setState({ categoryId: id, paid: false, selectedCards: [] })
  }, [])

  const setPaid = useCallback((paid: boolean) => {
    setState((s) => ({ ...s, paid }))
  }, [])

  const setSelectedCards = useCallback((cards: number[]) => {
    setState((s) => ({ ...s, selectedCards: cards }))
  }, [])

  const reset = useCallback(() => {
    setState(initialState)
    try {
      sessionStorage.removeItem(STORAGE_KEY)
    } catch {
      // Ignore private browsing or storage failures.
    }
  }, [])

  return (
    <FlowContext.Provider
      value={{ ...state, setCategory, setPaid, setSelectedCards, reset }}
    >
      {children}
    </FlowContext.Provider>
  )
}

export function useFlow() {
  const ctx = useContext(FlowContext)
  if (!ctx) throw new Error('useFlow must be used within FlowProvider')
  return ctx
}
