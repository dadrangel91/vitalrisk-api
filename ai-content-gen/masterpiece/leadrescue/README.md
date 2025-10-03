LeadRescue — MVP

LeadRescue converts missed calls and inquiries into booked appointments and 5★ reviews.

This repo contains a minimal FastAPI backend and a Next.js frontend stub, plus Docker/dev configs and marketing assets.

Quick start (full commands at the bottom):
- Backend: cd leadrescue/backend && python -m venv .venv; . .venv\Scripts\Activate.ps1; pip install -r requirements.txt; uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
- Frontend: cd leadrescue/frontend && npm install && npm run dev
- Docker: docker-compose up --build

See backend/README.md and frontend/README.md for details.
