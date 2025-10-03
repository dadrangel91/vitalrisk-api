from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class LeadCreate(BaseModel):
    name: Optional[str]
    phone: str
    message: Optional[str]
    source: Optional[str] = "web"

class LeadRead(BaseModel):
    id: int
    name: Optional[str]
    phone: str
    message: Optional[str]
    source: Optional[str]
    created_at: datetime
    status: str
    next_followup: Optional[datetime]

class BookingCreate(BaseModel):
    lead_id: int
    start: datetime
    end: datetime

class BusinessProfileUpdate(BaseModel):
    name: Optional[str]
    services: Optional[str]
    review_link: Optional[str]
    availability_json: Optional[str]
