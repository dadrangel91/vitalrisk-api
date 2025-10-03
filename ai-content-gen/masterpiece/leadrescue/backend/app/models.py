from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field

class Lead(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: Optional[str]
    phone: str
    message: Optional[str]
    source: Optional[str] = "web"
    created_at: datetime = Field(default_factory=datetime.utcnow)
    status: str = "new"
    next_followup: Optional[datetime] = None

class Booking(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    lead_id: int
    start: datetime
    end: datetime
    status: str = "tentative"

class BusinessProfile(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    services: Optional[str]
    review_link: Optional[str]
    availability_json: Optional[str]
