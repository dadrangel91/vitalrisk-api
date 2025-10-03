from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from datetime import datetime, timedelta
import os

from . import db
from .models import Lead, Booking, BusinessProfile
from .schemas import LeadCreate, LeadRead, BusinessProfileUpdate, BookingCreate
from .twilio_service import client as twilio_client
from .ai_assist import answer_faq
from sqlmodel import select

app = FastAPI(title="LeadRescue API")
app.add_middleware(CORSMiddleware, allow_origins=[os.getenv("FRONTEND_URL", "*")], allow_methods=["*"], allow_headers=["*"]) 

@app.on_event("startup")
def startup():
    db.init_db()

# Create lead (web form or missed call webhook)
@app.post("/api/leads", response_model=LeadRead)
def create_lead(lead: LeadCreate, background_tasks: BackgroundTasks):
    engine = db.init_db()
    session = db.get_session()
    l = Lead(name=lead.name, phone=lead.phone, message=lead.message, source=lead.source)
    session.add(l)
    session.commit()
    session.refresh(l)
    session.close()
    # send immediate SMS
    text = f"Hey {l.name or ''}, sorry we missed you — this is {os.getenv('BUSINESS_NAME','Business')}. We can help with {l.message or 'your request'}. Want to book or ask a question?"
    background_tasks.add_task(twilio_client.send_sms, l.phone, text)
    return l

# Inbound Twilio webhook for SMS replies
@app.post("/webhooks/twilio")
def inbound_sms(request: Request):
    # Twilio posts form data; for MVP read body raw
    form = await request.form()
    from_number = form.get('From')
    body = form.get('Body')
    # find lead by phone and mark replied
    session = db.get_session()
    stmt = select(Lead).where(Lead.phone == from_number)
    results = session.exec(stmt).all()
    if results:
        lead = results[0]
        lead.status = 'replied'
        session.add(lead)
        session.commit()
    # route to FAQ assistant
    slots = ['Today 2pm','Today 4pm']
    reply = answer_faq({}, body, slots)
    twilio_client.send_sms(from_number, reply)
    return {"ok": True}

# ... other endpoints truncated for brevity
@app.get("/api/leads", response_model=List[LeadRead])
def list_leads():
    session = db.get_session()
    stmt = select(Lead)
    rows = session.exec(stmt).all()
    return rows

@app.get("/api/leads/{lead_id}", response_model=LeadRead)
def get_lead(lead_id: int):
    session = db.get_session()
    lead = session.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="not found")
    return lead

@app.post("/api/leads/{lead_id}/complete")
def complete_lead(lead_id: int, background_tasks: BackgroundTasks):
    session = db.get_session()
    lead = session.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=404, detail="not found")
    lead.status = 'completed'
    session.add(lead)
    session.commit()
    # send immediate review request and schedule reminder in 48h
    review_link = os.getenv('BUSINESS_REVIEW_LINK','')
    text = f"Thanks for choosing {os.getenv('BUSINESS_NAME','Business')}! Mind dropping a quick review? {review_link}"
    background_tasks.add_task(twilio_client.send_sms, lead.phone, text)
    # schedule 48h reminder (APS scheduler not started here — in prod use background worker)
    return {"ok": True}
