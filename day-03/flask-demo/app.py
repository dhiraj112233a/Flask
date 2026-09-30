from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {
        "id": 1,
        "title": "Wings of Fire",
        "author": "Dr. APJ Kalam",
        "price": 450
    },
    {
        "id": 2,
        "title": "Vision 20-20",
        "author": "Dr. APJ Kalam",
        "price": 550
    }
]

@app.route("/api/books", methods=["GET"])
def get_books():
    return jsonify(books)

@app.route("/api/books", methods=["POST"])
def add_book():
    data = request.get_json()

    new_book = {
        "id": len(books) + 1,
        "title": data["title"],
        "author": data["author"],
        "price": data["price"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

if __name__ == "__main__":
    app.run(debug=True)