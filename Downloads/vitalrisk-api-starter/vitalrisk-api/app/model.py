
def score_risk(age: int, bmi: float, systolic_bp: int, smoker: bool, diabetic: bool) -> int:
    """
    Toy scoring function for demo purposes.
    Returns an integer 0-100.
    """
    score = 0
    # age contribution
    score += min(max((age - 30) * 0.7, 0), 35)
    # bmi contribution
    score += min(max((bmi - 22) * 1.2, 0), 25)
    # blood pressure contribution
    score += min(max((systolic_bp - 120) * 0.4, 0), 25)
    # lifestyle/conditions
    score += 8 if smoker else 0
    score += 12 if diabetic else 0
    return int(max(0, min(100, round(score))))

def label_risk(score: int) -> str:
    if score >= 70:
        return "High"
    if score >= 40:
        return "Moderate"
    return "Low"
