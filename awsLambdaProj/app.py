from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, ValidationError
from mangum import Mangum

app = FastAPI()

class CreditRiskRequest(BaseModel):
    income: float
    debt: float
    payment_history: float

@app.post("/credit")
async def calculate_credit_risk(request_data: CreditRiskRequest):
    try:
        # Some random logic to calculate credit risk score, for API demo purpose
        risk_score = request_data.income / (request_data.debt + 1) * request_data.payment_history

        return {
            "risk_score": risk_score,
            "message": "Credit risk score calculated successfully"
        }

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
    
handler = Mangum(app)