# AI Interview System

## Project Overview

This project is an AI-based Interview and Assessment System designed to automate candidate evaluation using audio, text, and monitoring pipelines.

The system performs:
- Speech-to-Text conversion
- AI-based answer evaluation
- Risk monitoring using camera detection
- Decision making for interview flow
- Final score and report generation

---

# Project Structure

```text
ai_interview_system/
│
├
├── audio/
├── video/
│── text/
└── questions.json
├── scores.json
├── logs.json
└── final_report.json
│
├──config.json
│
├── stt.py
├── llm_eval.py
├── detection.py
├── risk_engine.py
├── decision.py
└── tts.py
│── logger.py
│
├── main_pipeline.py
└── requirements.txt
```

---

# Modules Description

## stt.py
Handles Speech-to-Text conversion.

### Output Example
```json
{
  "text": "I have worked on machine learning models",
  "confidence": 0.9
}
```

---

## llm_eval.py
Evaluates answers using keyword matching and generates scores.

### Output Example
```json
{
  "score": 8.5,
  "feedback": "Keyword-based"
}
```

---

## detection.py
Simulates monitoring behavior detection.

### Output Example
```json
{
  "faces": 1,
  "eye_contact": true,
  "anomalies": []
}
```

---

## risk_engine.py
Calculates suspicious behavior risk score.

---

## decision.py
Determines next interview action.

Possible outputs:
- next_question
- repeat_question

---

## tts.py
Simulates Text-to-Speech output.

---

# Pipeline Flow

```text
User Audio
   ↓
Speech-to-Text
   ↓
Answer Evaluation
   ↓
Monitoring Detection
   ↓
Risk Calculation
   ↓
Decision Engine
   ↓
Final Report
```

---

# Installation

## Step 1
Extract the ZIP file.

## Step 2
Open terminal in project folder.

## Step 3
Install requirements:

```bash
pip install -r requirements.txt
```

---

# Run Project

```bash
python main_pipeline.py
```

---

# Output Files

| File | Purpose |
|------|----------|
| scores.json | Stores evaluation scores |
| logs.json | Stores system logs |
| final_report.json | Stores final interview results |

---

# Features

- Modular architecture
- JSON-based data handling
- Risk analysis support
- Interview automation
- Easy to extend

---

# Future Improvements

- Real Whisper STT integration
- OpenCV live webcam monitoring
- GPT-based evaluation
- Streamlit Web Interface
- Database support

---

# Technologies Used

- Python
- JSON
- Whisper (planned)
- OpenCV (planned)
- YOLO (planned)

---

# Author

AI Interview System Project

---

# License

This project is for academic and educational purposes.
