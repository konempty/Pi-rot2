import { copyFileSync, existsSync } from 'node:fs'
import { resolve } from 'node:path'

const indexPath = resolve('dist/index.html')
const fallbackPath = resolve('dist/404.html')

if (!existsSync(indexPath)) {
  throw new Error('dist/index.html does not exist. Run vite build first.')
}

copyFileSync(indexPath, fallbackPath)
console.log('Wrote dist/404.html for GitHub Pages SPA fallback.')
