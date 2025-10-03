LeadRescue Backend

Quick start:

1) Create a virtualenv and activate (PowerShell):

```powershell
python -m venv .venv
. .venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2) Copy `.env.sample` to `.env` and set TWILIO credentials and other secrets.

3) Run development server:

```powershell
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

4) Seed sample data:

```powershell
python scripts/seed.py
```

Files of interest:
- `app/` — FastAPI app
- `docker-compose.yml` and `Dockerfile` — dev containers
- `pyproject.toml` — packaging

