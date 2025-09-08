from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def get_numbers():
    numbers = [1, 2, 3, 4, 5]
    return jsonify(numbers)

if __name__ == '__main__':
    app.run(debug=True)