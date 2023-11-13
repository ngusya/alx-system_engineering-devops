#!/usr/bin/python3
import requests
from sys import argv
import sys

"""
access a url with employee ID to return information
"""

if __name__== "__main__":
    ID = int(argv[1])
    url="https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(ID)).json()
    tasks = []
    for task in todos:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(tasks), len(todos)))
    for task in tasks:
        print("\t {}".format(task))
