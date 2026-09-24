from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    # 1. Voter Eligibility
    age = 21

    # 2. Admin Dashboard
    user = {
        "name": "Dhiraj",
        "role": "admin"
    }

    # 3. Pass / Fail
    marks = [30, 50, 67, 24, 90]

    # 4. Stock
    stock_count = 54

    # 5. Odd / Even
    n = 35

    # 6. Login
    is_logged_in = True

    return render_template(
        "index1.html",
        age=age,
        user=user,
        marks=marks,
        stock_count=stock_count,
        n=n,
        is_logged_in=is_logged_in
    )


if __name__ == "__main__":
    app.run(debug=True)