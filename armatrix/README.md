# Armatrix Team Page

A full-stack **Team Page** for [Armatrix](https://armatrix.in) — a company building snake-like robotic arms for confined & hazardous spaces.

> **Frontend**: Next.js 14 (App Router) + Tailwind CSS + Framer Motion  
> **Backend**: Python + FastAPI + SQLite (SQLAlchemy ORM)

![Dark theme team page](https://img.shields.io/badge/theme-dark-111111) ![Next.js](https://img.shields.io/badge/Next.js-14-black) ![FastAPI](https://img.shields.io/badge/FastAPI-0.111-009688)

---

## ✨ Features

- **REST API** with full CRUD (Create, Read, Update, Delete) for team members
- **Auto-seeded database** with 6 sample team members on first startup
- **Armatrix-inspired design**: dark theme, green accent (#00ff88), glassmorphism cards, noise texture, grid background
- **Framer Motion animations**: staggered card reveals, hover lift, modal enter/exit
- **Responsive**: looks great on mobile, tablet, and desktop
- **Interactive**: Add/Edit/Delete team members via a polished modal form
- **Swagger Docs**: auto-generated at `/docs` for the backend

---

## 🚀 Quick Start

### Prerequisites
- **Node.js** 18+ and npm
- **Python** 3.10+

### 1. Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# Windows:
.\venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the server
uvicorn main:app --reload --port 8000
```

The API will be live at `http://localhost:8000` with Swagger docs at `http://localhost:8000/docs`.  
On first startup, the database is automatically seeded with 6 team members.

### 2. Frontend

```bash
cd frontend

# Install dependencies
npm install

# Run the dev server
npm run dev
```

The app will be live at `http://localhost:3000`.

> **Note**: The frontend expects the backend at `http://localhost:8000` by default.  
> To change this, set the `NEXT_PUBLIC_API_URL` environment variable:
> ```bash
> NEXT_PUBLIC_API_URL=https://your-backend.onrender.com npm run dev
> ```

---

## 🏗️ Project Structure

```
armatrix/
├── backend/
│   ├── main.py              # FastAPI app, CORS, startup seed
│   ├── database.py          # SQLite + SQLAlchemy setup
│   ├── models.py            # TeamMember SQLAlchemy model
│   ├── schemas.py           # Pydantic validation schemas
│   ├── seed.py              # Auto-seeds 6 sample members
│   ├── requirements.txt     # Python dependencies
│   └── routers/
│       └── team.py          # CRUD endpoints for /api/team
├── frontend/
│   ├── src/
│   │   ├── app/
│   │   │   ├── layout.tsx   # Root layout with SEO meta
│   │   │   ├── page.tsx     # Landing page (hero + feature cards)
│   │   │   ├── globals.css  # Design system (dark theme, glow, glass)
│   │   │   └── team/
│   │   │       └── page.tsx # Team page (grid, CRUD, loading/error states)
│   │   ├── components/
│   │   │   ├── Navbar.tsx           # Floating glassmorphic nav
│   │   │   ├── TeamMemberCard.tsx   # Member card w/ hover effects
│   │   │   └── TeamMemberFormModal.tsx  # Add/Edit form modal
│   │   └── lib/
│   │       └── api.ts       # Type-safe API client
│   └── ...
└── README.md
```

---

## 🎨 Design Decisions

### Visual Identity
- **Dark-first**: Pure black background (#050505) with subtle noise texture and grid pattern, mirroring the tech-forward feel of armatrix.in
- **Accent color**: Electric green (#00ff88) used consistently for CTAs, active nav states, social hover, and text highlights — inspired by Armatrix's brand palette
- **Glassmorphism**: Cards use `backdrop-filter: blur(20px)` with semi-transparent backgrounds and gradient borders for depth
- **Typography**: Space Grotesk for headings (techy, geometric), Inter for body text (clean, readable)

### Technical Choices
- **SQLite**: Zero-config persistent storage — perfect for a demo/assignment while being trivially replaceable with PostgreSQL for production
- **SQLAlchemy ORM**: Type-safe database operations with easy migration path
- **Framer Motion**: Declarative animations (stagger, spring physics, layout animations) that feel native and performant
- **Next.js App Router**: Modern file-based routing with React Server Components support, though this app uses `"use client"` pages for interactivity

### API Design
- `GET /api/team/` — List all members (ordered by `order` field)
- `GET /api/team/{id}` — Get single member
- `POST /api/team/` — Create member
- `PUT /api/team/{id}` — Partially update member
- `DELETE /api/team/{id}` — Remove member

All endpoints follow REST conventions with proper HTTP status codes (201 Created, 204 No Content, 404 Not Found).

---

## 🚢 Deployment

### Backend → Render / Railway
1. Push the `backend/` folder to a Git repo
2. On Render: Create a new **Web Service**, point to the repo, set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
3. Note the deployed URL (e.g., `https://armatrix-api.onrender.com`)

### Frontend → Vercel
1. Push the `frontend/` folder to a Git repo
2. On Vercel: Import the repo, set:
   - **Framework Preset**: Next.js
   - **Environment Variable**: `NEXT_PUBLIC_API_URL=https://your-backend-url.onrender.com`
3. Deploy!

---

## 📝 License

Built for the Armatrix Software Development Intern assignment.
