def evaluate_answer(question, answer, keywords):
    score = sum(1 for word in keywords if word in answer.lower())
    return {"score": (score/len(keywords))*10, "feedback": "Keyword-based"}
