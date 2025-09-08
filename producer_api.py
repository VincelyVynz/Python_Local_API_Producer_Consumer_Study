from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/numbers')
def get_numbers():
    numbers = [1, 2, 3, 4, 5]
    return jsonify(numbers)

@app.route('/products')
def get_products():
    products = [
        {"id": 1, "name"  : "Laptop" ,"price": 35000, "stock": 22},
        {"id": 2, "name" : "Wireless Mouse", "price": 890, "stock": 47},
        {"id": 3, "name" : "Mechanical Keyboard", "price": 1200, "stock": 50},
        {"id": 4, "name" : "Headphones", "price": 1500, "stock": 34},
        {"id": 5, "name" : "Cooling Pad", "price": 750, "stock": 8}
    ]
    return jsonify(products)


if __name__ == '__main__':
    app.run(debug=True)