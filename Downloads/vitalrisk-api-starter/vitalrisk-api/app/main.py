
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from .schemas import RiskRequest, RiskResponse
from .model import score_risk, label_risk

app = FastAPI(title="VitalRisk API", version="1.0.0", description="Simple demo API for health risk scoring. Not medical advice.")

# Open CORS for demo; tighten in prod
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/v1/risk", response_model=RiskResponse, summary="Calculate risk score", tags=["risk"])
def risk(req: RiskRequest):
    try:
        score = score_risk(req.age, req.bmi, req.systolic_bp, req.smoker, req.diabetic)
        return RiskResponse(risk_index=score, risk_label=label_risk(score))
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

# For dev run: uvicorn app.main:app --reload
