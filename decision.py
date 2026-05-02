def decide_next(score, risk):
    return "next_question" if (score - risk) >= 5 else "repeat_question"
