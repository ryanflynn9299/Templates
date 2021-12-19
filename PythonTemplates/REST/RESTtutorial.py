"""
A tutorial by Real Python
https://realpython.com/api-integration-in-python/

"""

import requests


def main():
    # ---------------- GET operation------------------------
    print("Performing GET operation")
    api_url = "https://jsonplaceholder.typicode.com/todos/1"
    resp = requests.get(api_url)
    print(resp.json())

    print(f"Response code: {resp.status_code}")
    print(f"Headers: {resp.headers}")

    print()

    # ----------------- POST operation ---------------------
    print("Performing POST operation")
    api_url = "https://jsonplaceholder.typicode.com/todos"
    post_json = {"userId": 1, "title": "Buy milk", "completed": False}
    # JSON to add a new to-do

    resp = requests.post(api_url, json=post_json)  # need to use json keyword arg or specify Content-Type header
    print(resp.json())

    print(f"Status code: {resp.status_code}")

    print()

    # ----------------- PUT operation -----------------------
    print("Performing PUT operation")
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    put_json = {"userId": 1, "title": "Mow Lawn", "completed": False}
    # JSON to overwrite to-do at index 10

    resp = requests.put(api_url, json=put_json)
    print(resp.json())

    print(f"Status code: {resp.status_code}")

    print()

    # ----------------- PATCH operation ----------------------
    print("Performing PATCH operation")
    api_url = "https://jsonplaceholder.typicode.com/todos/10"
    patch_json = {"title": "Wash car"}
    # JSON to modify title attribute of to-do at index 10

    resp = requests.patch(api_url, json=patch_json)
    print(resp.json())

    print(f"Status code: {resp.status_code}")


if __name__ == '__main__':
    main()
