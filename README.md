# AgriAssist — AI-Assisted Agriculture Web Application

A professional Flask prototype for an End Semester Exam (ESE) AI-assisted web application.

## Features
- Professional responsive agriculture dashboard
- AI-style Crop Advisor using crop, soil, growth stage and issue
- Preliminary Crop Health symptom screening
- Commodity Market Watch demo data
- Water-volume calculator
- Farm checklist
- Built-in agriculture chat assistant
- No API key required for the demo

## Run on Mac / VS Code

```bash
cd AgriAssist_Pro
python3 -m pip install -r requirements.txt
python3 app.py
```

Then open:

`http://127.0.0.1:5001`

## Project structure

```text
AgriAssist_Pro/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   └── index.html
└── static/
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
```

## Important academic note

The market values are clearly marked as demo data. The crop-health module is a preliminary screening feature, not a medical-style diagnosis system. For a real deployment, connect the advisor to a verified agricultural knowledge source or an AI API and add regional weather/soil/market APIs.
