#!/usr/bin/python3
"""
This module provides a script that sends a post request to a url as with
letters as parameters
"""

import requests
import sys

if __name__ == "__main__":
    try:
        search = sys.argv[1]
    except IndexError:
        search = ""
    data = {"q": search}
    res = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        d = res.json()
        if d is None:
            raise requests.JSONDecodeError

        if not d:
            print("No result")
        else:
            print("[{}] {}".format(d.get("id", ""), d.get("name", "")))
    except requests.JSONDecodeError as e:
        print("Not a valid JSON")
