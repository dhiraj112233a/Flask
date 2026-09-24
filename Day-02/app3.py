from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():

    profile = {
        "name": "Dhiraj",
        "city": "Pune Town",
        "skills": [
            "React",
            "Java",
            "SQL"
        ]
    }

    scores = [
        {
            "subject": "DSA",
            "marks": 88
        },
        {
            "subject": "JAVA",
            "marks": 92
        }
    ]

    posts = [
        {
            "title": "Flask Day 1",
            "author": "Jarvis",
            "views": 100000000
        }
    ]

    cart = {
        "Red Bull": 15,
        "Kurkure": 3
    }

    players = [
        {
            "name": "Dhiraj",
            "score": 95
        },
        {
            "name": "Sahil",
            "score": 85
        },
        {
            "name": "Atharva",
            "score": 92
        }
    ]

    directory = {
        "Frontend": [
            "React",
            "CSS"
        ],
        "Backend": [
            "Python",
            "Flask"
        ]
    }

    return render_template(
        "index.html",
        profile=profile,
        scores=scores,
        posts=posts,
        cart=cart,
        players=players,
        directory=directory
    )


if __name__ == "__main__":
    app.run(debug=True)