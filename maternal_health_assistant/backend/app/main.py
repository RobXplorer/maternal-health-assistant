from fastapi import FastAPI
from app.models import RiskInput, RiskOutput
from app.logic import assess_risk

app = FastAPI(title="Maternal Health Risk API")

@app.post("/predict", response_model=RiskOutput)
def predict_risk(input_data: RiskInput):
    result = assess_risk(
        bp=input_data.bp,
        fever=input_data.fever.lower(),
        bleeding=input_data.bleeding.lower(),
        headache=input_data.headache.lower(),
        convulsions=input_data.convulsions.lower()
    )
    return result
