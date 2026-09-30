from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {
        "name": "Rohit Sharma",
        "marks": 79,
        "status": "Pass"
    },
    {
        "name": "Virat Kohli",
        "marks": 32,
        "status": "Fail"
    }
]

@app.route("/api/students", methods=["GET"])
def get_students():
    return jsonify(students)

@app.route("/api/students", methods=["POST"])
def add_student():

    data = request.get_json()

    name = data["name"]
    marks = data["marks"]

    if marks >= 35:
        status = "Pass"
    else:
        status = "Fail"

    new_student = {
        "name": name,
        "marks": marks,
        "status": status
    }

    students.append(new_student)
    return jsonify(new_student), 201

if __name__ == "__main__":
    app.run(debug=True)