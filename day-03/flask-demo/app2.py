from flask import Flask, request, jsonify
app = Flask(__name__)

employees = [
    {
        "id": 1,
        "name": "Dhiraj",
        "department": "Gaming",
        "salary": 45000
    },
    {
        "id": 2,
        "name": "Sahil",
        "department": "IT",
        "salary": 40000
    }
]

@app.route("/api/emp", methods=["GET"])
def get_employees():
    return jsonify(employees)

@app.route("/api/emp", methods=["POST"])
def add_employee():

    data = request.get_json()

    new_employee = {
        "id": len(employees) + 1,
        "name": data["name"],
        "department": data["department"],
        "salary": data["salary"]
    }

    employees.append(new_employee)

    return jsonify(new_employee), 201

if __name__ == "__main__":
    app.run(debug=True)