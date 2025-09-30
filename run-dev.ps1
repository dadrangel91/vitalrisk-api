# run-dev.ps1 — start VitalRisk API locally

Write-Host "=== Starting VitalRisk API ==="

# Create venv if missing
if (-Not (Test-Path ".venv")) {
    Write-Host "Creating virtual environment..."
    py -m venv .venv
}

# Activate venv (PowerShell)
Write-Host "Activating venv..."
. .\.venv\Scripts\Activate.ps1

# Install deps
Write-Host "Installing requirements..."
pip install -r requirements.txt

# Run API
Write-Host "Launching Uvicorn server on http://127.0.0.1:8000 ..."
uvicorn app.main:app --reload
