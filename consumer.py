import requests

def consumer_numbers():
    response = requests.get("http://127.0.0.1:5000/numbers")
    if response.status_code == 200:
        numbers = response.json()
        for number in numbers:
            print(number)
    else:
        print(f"Something went wrong.\nStatus code: {response.status_code}")

def consumer_products():
    try:
        response = requests.get("http://127.0.0.1:5000/products")
        response.raise_for_status()
        products = response.json()
        for product in products:
            if product["stock"] > 30:
                print(f"{product["name"]} : {product['stock']}  in stock")

    except Exception as e:
        print(e)

def consumer_tasks():
    try:
        response = requests.get("http://127.0.0.1:5000/tasks")
        response.raise_for_status()
        tasks = response.json()
        for task in tasks:
            print(task)

    except Exception as e:
        print(e)

def high_priority_tasks():
    try:
        response = requests.get("http://127.0.0.1:5000/tasks")
        response.raise_for_status()
        tasks = response.json()
        for task in tasks:
            if task["priority"] == "high":
                print(task["description"])
    except Exception as e:
        print(e)

if __name__ == '__main__':
    # consumer_numbers()
    # consumer_products()
    # consumer_tasks()
    high_priority_tasks()