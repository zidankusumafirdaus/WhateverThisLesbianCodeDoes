# Frontend Project Structure

## Directory Tree
```
FrontEnd/
├── public/                          # Static assets
│   └── [favicon, images, etc]
├── src/
│   ├── assets/                      # Reusable media files (images, icons, fonts)
│   ├── components/                  # Reusable React components
│   │   └── [other components]
│   ├── hooks/                       # Custom React hooks
│   │   └── [other hooks]
│   ├── pages/                       # Page components (route level)
│   │   └── [other pages]
│   ├── service/                     # API calls and external service integrations
│   │   ├── api.js
│   │   └── [other services]
│   ├── styles/                      # Global and shared styles
│   │   └── index.css
│   ├── utils/                       # Utility functions and helpers
│   │   ├── example.jsx
│   │   └── [other utilities]
│   └── routes.jsx                   # Application routing setup
├── tailwind.config.js               # Tailwind CSS configuration
├── package.json                     # Project dependencies and scripts
```

---

## Folder Definitions & Responsibilities

### `/public`
**Purpose:** Static assets yang tidak di-process oleh bundler
- Favicon, images statis, fonts, dokumentasi publik
- File di sini tidak di-hash dan langsung di-copy ke output
- Akses via `/filename` di HTML atau JavaScript

### `/src/assets`
**Purpose:** Media files yang diimport dalam komponen
- Gambar, ikon, animasi, fonts custom
- Akan di-process dan di-hash oleh Vite
- Digunakan melalui import statements

### `/src/components`
**Purpose:** Reusable UI components
- Presentational components (stateless atau minimal state)
- Contoh: Button, Card, Header, Footer, Modal, Form inputs
- Setiap komponen harus self-contained dan dapat digunakan di berbagai halaman
- File dinamis - growth area untuk aplikasi

### `/src/hooks`
**Purpose:** Custom React hooks untuk logic reusable
- State management logic
- API integration logic
- Form handling, authentication, browser APIs
- Contoh: `useAuth()`, `useFetch()`, `useForm()`, `useLocalStorage()`
- Prefix nama dengan `use` untuk mengikuti React convention

### `/src/pages`
**Purpose:** Route-level page components
- Component untuk setiap route/page
- Dapat meng-compose multiple `components` dan menggunakan `hooks`
- Contoh: `app.jsx`, `dashboard.jsx`, `profile.jsx`, `notFound.jsx`
- Directly mapped dalam `routes.jsx`

### `/src/service`
**Purpose:** Business logic, API calls, dan external integrations
- API client setup dan interceptors
- Service functions untuk fetch data
- External service integrations (payment, auth, etc)
- Contoh: `api.js`, `auth.js`, `payment.js`, `analytics.js`
- **Tidak mengandung React components**

### `/src/styles`
**Purpose:** Global styling dan theme definitions
- Global CSS styles
- Tailwind directives dan custom utilities
- Theme variables (colors, spacing, fonts)
- Reset styles, animations
- Diimport sekali di `routes.jsx` untuk tersedia global

### `/src/utils`
**Purpose:** Pure utility functions dan helpers
- Bukan React components atau hooks
- Contoh: `formatDate()`, `validateEmail()`, `calculateDiscount()`, `parseError()`
- Dapat digunakan di mana saja (components, services, pages)
- Harus pure functions untuk predictability dan testability

### `/src/routes.jsx`
**Purpose:** Konfigurasi routing aplikasi
- Definisi semua routes dengan components
- React Query client setup
- Provider setup (Router, QueryClientProvider, dll)
- Entry point untuk rendering React app

---

## Aturan Penulisan (Convention)
### Naming Conventions

| Type | Convention | Example |
|------|-----------|---------|
| React Components | PascalCase, .jsx | `UserProfile.jsx`, `ProductCard.jsx` |
| Custom Hooks | camelCase with `use` prefix, .js/.jsx | `useAuth.js`, `useFetchData.js` |
| Pages | PascalCase, .jsx | `Dashboard.jsx`, `NotFound.jsx` |
| Services | camelCase, .js | `api.js`, `authService.js` |
| Utilities | camelCase, .js | `formatDate.js`, `validateEmail.js` |
| Folders | camelCase | `src/components`, `src/hooks` |
| Constants | UPPER_SNAKE_CASE | `API_BASE_URL`, `MAX_RETRIES` |
| Boolean variables | Prefix with `is`, `has`, `can`, `should` | `isLoading`, `hasError`, `canEdit` |