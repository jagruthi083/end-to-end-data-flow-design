import json
from modules.stt import speech_to_text
from modules.llm_eval import evaluate_answer
from modules.detection import detect_behavior
from modules.risk_engine import calculate_risk
from modules.decision import decide_next
from modules.tts import text_to_speech

with open("data/text/questions.json") as f:
    questions = json.load(f)

results = []

for q in questions:
    stt = speech_to_text("data/audio/sample.wav")
    eval_out = evaluate_answer(q["question"], stt["text"], q["expected_keywords"])
    detect = detect_behavior("data/video/sample.mp4")
    risk = calculate_risk(detect)
    decision = decide_next(eval_out["score"], risk["risk_score"])

    results.append({
        "question": q["question"],
        "answer": stt["text"],
        "score": eval_out["score"],
        "risk": risk["risk_score"],
        "decision": decision
    })

with open("outputs/final_report.json","w") as f:
    json.dump(results,f,indent=2)

print("Pipeline completed")
