import mailparser
from datetime import datetime

def process_email(raw_email):
    mail = mailparser.parse_from_string(raw_email)
    sender = mail.from_[0][1]
    subject = mail.subject
    body = mail.body

    # Classify intent
    intent = classifier(body, ["Invoice", "RFQ", "Complaint", "Regulation"])["labels"][0]
    
    # Simple urgency detection
    urgency = "High" if any(word in body.lower() for word in ["urgent", "asap", "immediately"]) else "Normal"

    return {
        "sender": sender,
        "intent": intent,
        "urgency": urgency,
        "received": mail.date.isoformat() if mail.date else datetime.utcnow().isoformat()
    }
