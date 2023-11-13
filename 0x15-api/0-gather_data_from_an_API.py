#!/usr/bin/python3

"""
 Script that, using this REST API, for a given employee ID,
 returns information about his/her
 todo list progress
 """

import requests
import sys

"""
access a url with employee ID to return information
"""

if __name__ == "__main__":
    ID = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos?userId={}".format(ID)).json()
    
    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]
    