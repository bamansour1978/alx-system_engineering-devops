#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "user/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()

    completed = [j.get("title") for j in todos if j.get("completed") is True]
    print("Employee {} is done with task({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(com)) for com in completed]
