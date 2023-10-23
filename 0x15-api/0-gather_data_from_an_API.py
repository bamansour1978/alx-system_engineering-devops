#!/usr/bin/python3
"""
script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
import sys

if __name__ == "__main__":
    urll = "https://jsonplaceholder.typicode.com/"
    user = requests.get(urll + "user/{}".format(sys.argv[1])).json()
    tod = requests.get(urll + "todos", parms={"userId": sys.argv[1]}).json()

    completed = [to.get("title") for to in tod if to.get("completed") is True]
    print("Employee {} is done with task({}/{}):".format(
        user.get("name"), len(completed), len(tod)))
    [print("\t {}".format(com)) for com in completed]
