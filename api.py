from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="BankShield AI Fraud Detection API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Transaction(BaseModel):
    amount: float
    hour: int
    merchantRisk: str
    international: bool
    cardPresent: bool

def dummy_predict(tx: Transaction) -> float:
    score = 0.05
    if tx.amount > 3000:
        score += 0.40
    elif tx.amount > 2000:
        score += 0.30
    elif tx.amount > 1000:
        score += 0.15

    if 1 <= tx.hour <= 5:
        score += 0.35
    elif 22 <= tx.hour <= 23 or 0 <= tx.hour <= 6:
        score += 0.15

    if tx.merchantRisk == "high":
        score += 0.35
    elif tx.merchantRisk == "medium":
        score += 0.15

    if tx.international:
        score += 0.25
    if not tx.cardPresent:
        score += 0.30

    if tx.amount > 2000 and not tx.cardPresent:
        score += 0.20
    if tx.international and tx.merchantRisk == "high":
        score += 0.20
    if tx.amount > 2000 and (1 <= tx.hour <= 5):
        score += 0.20

    return min(max(score, 0.01), 0.99)

@app.post("/predict")
async def predict(tx: Transaction):
    prob = dummy_predict(tx)
    return {"fraud_probability": float(prob)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)