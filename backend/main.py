from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Customer Inquiry Triage API")

class Inquiry(BaseModel):
    message: str

def classify_message(message: str):
    msg = message.lower()

    if any(word in msg for word in ["error", "bug", "crash", "log in", "password"]):
        return "TECHNICAL_SUPPORT", "Message mentions a login or technical issue.", 0.95
    elif any(word in msg for word in ["invoice", "payment", "refund", "billing", "price"]):
        return "BILLING_INQUIRY", "Billing or payment-related terms found.", 0.9
    elif any(word in msg for word in ["buy", "purchase", "demo", "pricing plan"]):
        return "SALES", "Pre-purchase interest detected.", 0.85
    elif ("cancel" in msg and "account" in msg) or \
         ("update" in msg and "info" in msg) or \
         ("change" in msg and "plan" in msg):
        return "ACCOUNT_MANAGEMENT", "Request to update or manage account.", 0.9
    elif any(word in msg for word in ["feedback", "suggestion", "great job", "complaint"]):
        return "GENERAL_FEEDBACK", "General user comment or feedback.", 0.8
    else:
        return "GENERAL_FEEDBACK", "No strong match, defaulted to feedback.", 0.5

@app.post("/triage")
def triage(inquiry: Inquiry, minimal: bool = False):
    category, reasoning, score = classify_message(inquiry.message)

    if minimal:
        return {"category": category}

    return {"category": category, "reasoning": reasoning, "score": score}

