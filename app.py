
from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Safely load the model and scaler
try:
    model = pickle.load(open("election_model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
except Exception as e:
    print("⚠️ Model or Scaler loading failed:", e)
    model = None
    scaler = None

@app.route("/", methods=["GET", "POST"])
def predict():
    prediction = ""

    # Full dummy analytics data to match template expectations
    default_stats = {
        "accuracy_metrics": {
            "total_predictions": 0,
            "correct": 0,
            "accuracy": "0%",
            "win_predictions": 0
        }
    }

    if request.method == "POST":
        if model is None or scaler is None:
            prediction = "Model or Scaler not available. Please try again later."
        else:
            try:
                age = float(request.form["age"])
                income = float(request.form["income"])
                education = float(request.form["education"])
                gender = 1 if request.form["gender"] == "Male" else 0
                region = int(request.form["region"])

                features = np.array([[age, income, education, gender, region]])
                scaled = scaler.transform(features)
                result = model.predict(scaled)

                prediction = "Yes" if result[0] == 1 else "No"
            except Exception as e:
                prediction = f"Error: {str(e)}"

    return render_template("index.html", result=prediction, analytics=default_stats)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
