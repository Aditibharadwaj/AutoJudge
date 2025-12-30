from flask import Flask, render_template, request
import joblib
import pandas as pd

def combine_text(X):
    return (
        X["problem_description"].astype(str) + " " +
        X["input_description"].astype(str) + " " +
        X["output_description"].astype(str)
    )

app = Flask(__name__)

# Load trained models
clf = joblib.load("models/difficulty_classifier.pkl")
reg = joblib.load("models/difficulty_regressor.pkl")
le  = joblib.load("models/label_encoder.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        description = request.form["description"]
        input_desc  = request.form["input_desc"]
        output_desc = request.form["output_desc"]

        X_input = pd.DataFrame([{
            "problem_description": description,
            "input_description": input_desc,
            "output_description": output_desc
        }])

        class_id = clf.predict(X_input)[0]
        class_name = le.inverse_transform([class_id])[0]
        score = reg.predict(X_input)[0]

        prediction = {
            "class": class_name,
            "score": round(float(score), 2)
        }

    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
