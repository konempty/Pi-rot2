import React from 'react'
import { createRoot } from 'react-dom/client'
import { App } from '@/App'
import { FlowProvider } from '@/components/flow-provider'
import { I18nProvider } from '@/lib/i18n'
import '@/styles.css'

createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <I18nProvider>
      <FlowProvider>
        <App />
      </FlowProvider>
    </I18nProvider>
  </React.StrictMode>,
)
