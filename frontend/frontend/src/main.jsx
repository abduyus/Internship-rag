import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import GlobalStyles from './GlobalStyles.js'


document.documentElement.classList.add('dark-mode')

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <GlobalStyles />
    <App />
  </StrictMode>,
)
