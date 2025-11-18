AI-Based Health Risk Predictor & Diet Coach

(Flask + Machine Learning + Scikit-learn)

This is a Machine Learning–powered web application that predicts potential health risks based on user inputs such as age, weight, height, BMI, lifestyle habits, etc.
Along with prediction, the system also provides personalized diet and lifestyle recommendations to help users improve their overall health.

🚀 Features
Predicts health risk (Low / Medium / High)
Takes user inputs (age, BMI, weight, lifestyle habits)
ML model trained using Scikit-learn
Real-time prediction using Flask API
Personalized diet and lifestyle suggestions
Simple and clean user interface (HTML/CSS)


health-risk-predictor/
│
├── app/
│   ├── main.py               # Flask server (routes + prediction)
│   ├── model_utils.py        # Loads ML model + preprocessing + prediction logic
│   ├── model/
│   │   └── health_model.pkl  # Trained ML model
│   │
│   ├── static/
│   │   ├── style.css         # UI styling
│   │   └── script.js         # (optional)
│   │
│   └── templates/
│       └── index.html        # Input form UI
│
├── requirements.txt
└── README.md



