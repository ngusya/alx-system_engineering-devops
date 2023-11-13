#!/usr/bin/python3

"""
 Script that, using this REST API, for a given employee ID,
 returns information about his/her
 todo list progress
 """

import requests
from sys import argv
import sys

"""
access a url with employee ID to return information
"""

if __name__ == "__main__":
    ID = int(argv[1])
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(ID)).json()
    tasks = []
    for task in todos:
        if task.get('completed') is True:
            tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(tasks), len(todos)))
    for task in tasks:
        print("\t {}".format(task))
