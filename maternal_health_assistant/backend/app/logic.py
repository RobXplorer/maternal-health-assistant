def assess_risk(bp: str, fever: str, bleeding: str, headache: str, convulsions: str):
    # Parse blood pressure
    try:
        systolic, diastolic = map(int, bp.split('/'))
    except Exception:
        return {
            "risk_level": "unknown",
            "recommendation": "Invalid BP format. Please enter as '120/80'."
        }

    # Simple rule-based logic
    if systolic > 140 or diastolic > 90 or bleeding == "yes" or convulsions == "yes":
        return {
            "risk_level": "high",
            "recommendation": "Seek immediate medical attention at the nearest facility."
        }

    if fever == "yes" or headache == "yes":
        return {
            "risk_level": "moderate",
            "recommendation": "Monitor symptoms. Visit a clinic if conditions worsen."
        }

    return {
        "risk_level": "low",
        "recommendation": "Continue regular antenatal care. No urgent risks detected."
    }
