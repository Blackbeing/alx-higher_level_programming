#!/usr/bin/python3
"""
This module provides a script that sends a GET request to github API
and returns user information
"""
import requests
import sys

if __name__ == "__main__":
    user, pat = sys.argv[1:]
    res = requests.get(
        "https://api.github.com/user",
        auth=requests.auth.HTTPBasicAuth(user, pat),
    )
    print(res.json().get("id", ""))
