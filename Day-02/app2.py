from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    fruits = [
        "Apple",
        "Banana",
        "Mango"
    ]

    students = [
        "Rohit",
        "Virat",
        "Dhoni",
        "Sachin",
        "Kapil"
    ]

    products = [
        {
            "name": "Iphone Duo",
            "price": 450000
        },
        {
            "name": "Dell G15",
            "price": 80000
        }
    ]
    items = []
    tasks = [
        "Hey",
        "Hello",
        "Namaste",
        "Hii",
        "Hlw"
    ]

    numbers = [
        45,4,24,34,45,6,3
    ]

    return render_template(
        "index2.html",
        fruits=fruits,
        students=students,
        products=products,
        items=items,
        tasks=tasks,
        numbers=numbers
    )
if __name__ == "__main__":
    app.run(debug=True)