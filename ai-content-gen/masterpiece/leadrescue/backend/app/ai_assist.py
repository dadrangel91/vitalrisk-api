from typing import Dict, List

# Small prompt bank for LLM assistance (integrate later with an LLM provider)
SYSTEM_PROMPTS = {
    "faq_answer": (
        "You are a polite scheduling assistant for {BUSINESS}. Using {BUSINESS_PROFILE}, "
        "answer the user's question briefly (<=2 sentences), then offer 2 booking windows: {SLOTS}. "
        "If the user asks for pricing, give a reasonable range and say final quote is provided on call. "
        "Never provide medical or legal advice."
    )
}


def answer_faq(business_profile: Dict, lead_message: str, slots: List[str]) -> str:
    # For MVP we keep this deterministic: use canned reply based on keywords
    if "price" in (lead_message or "").lower() or "cost" in (lead_message or "").lower():
        price = business_profile.get("services", "service")
        return f"Typical pricing for {price} starts around $100-$300; final quote on a call. We can book {slots[0]} or {slots[1]}."
    # fallback polite reply
    return f"Thanks — we can help. Available: {slots[0]} or {slots[1]}. Reply 'book' to secure a slot."
