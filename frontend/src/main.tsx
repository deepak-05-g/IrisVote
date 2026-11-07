import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.tsx'
import Register from './pages/Register.tsx'

const root = document.getElementById('root')!;
createRoot(root).render(
  <StrictMode>
    {window.location.pathname === "/register" ? <Register /> : <App />}
  </StrictMode>,
)
