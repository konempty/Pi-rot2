import { LANGUAGES, useI18n, type Language } from '@/lib/i18n'

const introCopy: Record<Language, { title: string; desc: string }> = {
  en: {
    title: 'Choose your language',
    desc: 'You can change it later from the top-right menu.',
  },
  ko: {
    title: '언어를 선택하세요',
    desc: '나중에 우측 상단 메뉴에서 다시 변경할 수 있습니다.',
  },
  ja: {
    title: '言語を選択してください',
    desc: 'あとで右上のメニューから変更できます。',
  },
  zh: {
    title: '请选择语言',
    desc: '之后可以在右上角菜单中更改。',
  },
}

export function LanguageWelcomeModal() {
  const { hasSelectedLanguage, setLanguage } = useI18n()

  if (hasSelectedLanguage) return null

  return (
    <div className="fixed inset-0 z-[100] flex items-center justify-center bg-background/80 px-5 backdrop-blur-md">
      <div className="w-full max-w-md rounded-3xl border border-primary/30 bg-card/95 p-6 shadow-2xl shadow-black/40">
        <div className="text-center">
          <p className="text-xs font-medium uppercase tracking-[0.22em] text-primary/80">
            PI-rot Tarot
          </p>
          <h2 className="mt-3 font-serif text-3xl font-bold text-foreground">
            Choose Language
          </h2>
          <p className="mt-2 text-sm leading-relaxed text-muted-foreground">
            Select once to begin. You can change language anytime from the top-right menu.
          </p>
        </div>

        <div className="mt-6 grid gap-2">
          {LANGUAGES.map((language) => (
            <button
              key={language.code}
              type="button"
              onClick={() => setLanguage(language.code)}
              className="flex items-center gap-3 rounded-2xl border border-border bg-background/40 px-4 py-3 text-left transition hover:border-primary/60 hover:bg-primary/10"
            >
              <span className="text-2xl" aria-hidden="true">
                {language.flag}
              </span>
              <span className="min-w-0">
                <span className="block font-medium text-foreground">
                  {language.nativeLabel}
                </span>
                <span className="block text-xs text-muted-foreground">
                  {introCopy[language.code].title} · {introCopy[language.code].desc}
                </span>
              </span>
            </button>
          ))}
        </div>
      </div>
    </div>
  )
}
