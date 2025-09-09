from flask import Flask
import requests
app = Flask(__name__)

@app.route('/show_tasks')
def show_tasks():
    try:
        response = requests.get("http://localhost:5000/tasks")
        response.raise_for_status()
        tasks = response.json()
        print(tasks)
        return tasks
    except requests.exceptions.RequestException as e:
        print(e)
        return  e

@app.route('/get_products')
def get_products():
    try:
        response = requests.get("http://127.0.0.1:5000/products")
        response.raise_for_status()
        products = response.json()
        print(products)
        return products

    except requests.exceptions.RequestException as e:
        print(e)
        return e

if __name__ == '__main__':
    app.run(debug=True, port=5001)