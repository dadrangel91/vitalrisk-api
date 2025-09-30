
from pydantic import BaseModel, Field, confloat, conint

class RiskRequest(BaseModel):
    age: conint(ge=0, le=120) = Field(..., description="Age in years")
    bmi: confloat(ge=10, le=60) = Field(..., description="Body Mass Index")
    systolic_bp: conint(ge=70, le=240) = Field(..., description="Systolic blood pressure (mmHg)")
    smoker: bool = Field(..., description="Current smoker?")
    diabetic: bool = Field(..., description="Diagnosed diabetic?")

class RiskResponse(BaseModel):
    risk_index: conint(ge=0, le=100)
    risk_label: str
