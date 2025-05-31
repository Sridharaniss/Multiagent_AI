from pydantic import BaseModel, ValidationError

class TargetSchema(BaseModel):
    company_name: str
    rfq_id: str
    items: list

def process_json(json_data):
    try:
        data = TargetSchema(**json_data)
        anomalies = []
    except ValidationError as e:
        anomalies = e.errors()
        data = None
    return data, anomalies
