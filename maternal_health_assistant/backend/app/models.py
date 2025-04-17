from pydantic import BaseModel

class RiskInput(BaseModel):
    bp: str  # e.g., "150/95"
    fever: str  # "yes" or "no"
    bleeding: str
    headache: str
    convulsions: str

class RiskOutput(BaseModel):
    risk_level: str  # "low", "moderate", "high"
    recommendation: str
