
# VitalRisk API

A tiny FastAPI service that calculates a demo health risk score. Great for showcasing an ML/API workflow and collecting early interest.

> ⚠️ **Not medical advice. Educational/demo only.**

## Quickstart (Local)

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open: http://127.0.0.1:8000/docs

Run tests:

```bash
pytest -q
```

## Docker

```bash
docker build -t vitalrisk:latest .
docker run -p 8000:8000 vitalrisk:latest
```

## Endpoints

- `GET /health` → `{ "status": "ok" }`
- `POST /v1/risk` → `{ "risk_index": int(0..100), "risk_label": "Low|Moderate|High" }`

**Payload example:**

```json
{
  "age": 55,
  "bmi": 28.5,
  "systolic_bp": 138,
  "smoker": true,
  "diabetic": false
}
```

## Demo Frontend

Open `frontend/index.html` in a browser. Set your API base URL and try it live.

## Deploy (Render/Railway via Docker)

1. Push this folder to a new GitHub repo.
2. In Render or Railway, choose "Deploy from repo" and select Docker.
3. Expose port **8000**. Health check path: `/health`.
4. Add environment variable `ENV=prod` (optional).

## Positioning

- **Name:** VitalRisk API
- **Tagline:** *Turn raw vitals into a simple risk signal in seconds.*
- **Use-cases:** triage prototypes, analytics demos, hackathon demos, teaching.

## Pricing (starter idea)

- Free (1k calls/month)
- Starter $19/mo (100k calls)
- Growth $99/mo (2M calls)
- Custom/On‑prem: contact

## Legal / Safety

This service is not a medical device and not intended for diagnosis or treatment.
