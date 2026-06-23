import { LANGUAGES, useI18n, type Language } from '@/lib/i18n'

export function LanguageSelector() {
  const { language, setLanguage, t } = useI18n()

  return (
    <label className="inline-flex items-center gap-2 rounded-full border border-primary/30 bg-card/70 px-3 py-1.5 text-xs font-medium text-primary shadow-sm backdrop-blur">
      <span className="sr-only">{t('language')}</span>
      <select
        value={language}
        onChange={(event) => setLanguage(event.target.value as Language)}
        className="max-w-28 appearance-none bg-transparent text-primary outline-none"
        aria-label={t('language')}
      >
        {LANGUAGES.map((item) => (
          <option key={item.code} value={item.code} className="bg-background text-foreground">
            {item.flag} {item.nativeLabel}
          </option>
        ))}
      </select>
    </label>
  )
}
