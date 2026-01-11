from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

with open("model/trained_model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route ("/", methods = ["GET", "POST"])
def index():

    prediction = None

    if request.method == "POST":
        study_hours = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        sleep_hours = float(request.form["sleep_hours"])
        screen_time = float(request.form["screen_time"])
        previous_score = float(request.form["previous_score"])


        input_data = np.array(
            [[study_hours, attendance, sleep_hours, screen_time, previous_score]]
        )

        result = model.predict(input_data)[0]

        prediction = (
            "Student will perform WELL! 🎓"
            if result == 1
            else "Student may perform POORLY!⚠️"
        )


    return render_template("index.html", prediction = prediction)
    

if __name__ == "__main__":
    app.run(debug = True)