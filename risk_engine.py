def calculate_risk(detection):
    risk = 0
    if detection["faces"] > 1:
        risk += 0.5
    if not detection["eye_contact"]:
        risk += 0.3
    return {"risk_score": risk}
