import requests

def consumer():
    response = requests.get("http://127.0.0.1:5000/")
    if response.status_code == 200:
        numbers = response.json()
        for number in numbers:
            print(number)
    else:
        print(f"Something went wrong.\nStatus code: {response.status_code}")

if __name__ == '__main__':
    consumer()