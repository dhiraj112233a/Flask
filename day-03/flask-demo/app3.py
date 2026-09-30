from flask import Flask, request, jsonify

app = Flask(__name__)

cart = []


@app.route("/api/cart", methods=["POST"])
def add_to_cart():

    data = request.get_json()

    product_name = data.get("product_name")
    price = data.get("price")

    if price is None or price <= 0:
        return jsonify({
            "message": "Invalid price"
        }), 400

    product = {
        "product_name": product_name,
        "price": price
    }

    cart.append(product)

    return jsonify({
        "message": "Product added successfully",
        "product": product
    }), 201


if __name__ == "__main__":
    app.run(debug=True)