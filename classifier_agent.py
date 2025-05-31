import mimetypes
from email import message_from_string
from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def classify_input(raw_input):
    # Detect format
    if isinstance(raw_input, dict):
        fmt = "JSON"
    elif raw_input.strip().startswith("From:"):
        fmt = "Email"
    elif raw_input.endswith(".pdf"):
        fmt = "PDF"
    else:
        fmt = "Unknown"

    # Extract content for NLP classification
    content = extract_text_from_input(raw_input, fmt)

    # Predict intent
    labels = ["Invoice", "RFQ", "Complaint", "Regulation"]
    result = classifier(content, labels)
    intent = result['labels'][0]

    return fmt, intent
