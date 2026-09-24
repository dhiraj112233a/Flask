from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
@app.route("/")
def home():
    app_name = "My First Flask App"
    age = 21
    current_year = datetime.now().year
    student_name = "Dhiraj"
    score = 85

    return render_template(
        "index.html",
        app_name=app_name,
        age=age,
        current_year=current_year,
        student_name=student_name,
        score=score
    )
if __name__ == "__main__":
    app.run(debug=True)