
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_risk():
    payload = {"age": 55, "bmi": 28.5, "systolic_bp": 138, "smoker": True, "diabetic": False}
    r = client.post("/v1/risk", json=payload)
    assert r.status_code == 200
    body = r.json()
    assert "risk_index" in body and "risk_label" in body
