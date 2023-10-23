#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python
script to export data in the JSON format.
"""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            us.get("id"): [{
                "task": ti.get("title"),
                "completed": ti.get("completed"),
                "username": us.get("username")
            } for ti in requests.get(url + "todos",
                                     params={"userId": us.get("id")}).json()]
            for us in users}, jsonfile)
