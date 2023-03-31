#!/usr/bin/python3
"""
This module provides a script that takes url argument, fetches url
and displays contest of X-Request-Id variable
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with requests.get(url) as res:
        print(res.headers.get("X-Request-Id"))
