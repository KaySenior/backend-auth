# Zentrio CRM Frontend

The frontend for the Zentrio CRM project. It is a React application powered by Vite.

## Project Structure

```text
frontend/
├── public/
│   └── .gitkeep
├── src/
│   ├── api/              # API clients and request helpers
│   │   └── .gitkeep
│   ├── assets/           # Images, icons, and other imported assets
│   │   └── .gitkeep
│   ├── components/       # Reusable React components
│   │   └── .gitkeep
│   ├── pages/            # Page-level views and routes
│   │   └── .gitkeep
│   ├── App.css           # App-level styles
│   ├── App.jsx           # Root application component
│   ├── index.css         # Global styles
│   └── main.jsx          # Application entry point
├── index.html            # Vite HTML entry point
├── eslint.config.js      # ESLint configuration
├── vite.config.js        # Vite configuration
├── package.json          # Scripts and dependencies
└── package-lock.json     # Locked dependency versions
```

## Getting Started

From the `frontend` directory, install dependencies and start the development server:

```bash
npm install
npm run dev
```

## Available Scripts

| Command | Description |
| --- | --- |
| `npm run dev` | Start the Vite development server with hot reload. |
| `npm run build` | Create a production build. |
| `npm run preview` | Preview the production build locally. |
| `npm run lint` | Run ESLint across the frontend. |

## Current Status

The application shell is in place. The CRM API layer, reusable components, page views, and imported assets will be added to their respective directories as the product is implemented.
