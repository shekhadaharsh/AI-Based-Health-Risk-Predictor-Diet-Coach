from flask import Flask, render_template, request
import pickle
import numpy as np

from diet import get_diet_plan
app = Flask(__name__)

# load trained model
model = pickle.load(open("health_model.pkl", "rb"))

# mapping result
risk_mapping = {0: "Low", 1: "Medium", 2: "High"}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        age = float(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"]) / 100 
        smoking = int(request.form["smoking"])
        activity = int(request.form["activity"])
        disease = int(request.form["disease"])
        diet = int(request.form["diet"])

        # calculate BMI
        bmi = weight / (height ** 2)

        # features array (same order as training)
        features = np.array([[age, weight, height*100, bmi, smoking, activity, disease, diet]])

        # predict
        prediction = model.predict(features)[0]
        risk_result = risk_mapping[prediction]

        personalized_diet=get_diet_plan(bmi, activity, disease, diet)
        return render_template("result.html", 
                               prediction_text=f"Your Health Risk Level is: {risk_result}",
                               diet=personalized_diet,
                               bmi=round(bmi,2))

if __name__ == "__main__":
    app.run(debug=True)
