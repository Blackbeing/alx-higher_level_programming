#!/usr/bin/python3
"""
This module provides a script that takes in url as argument, sends a
request and prints body of response decoded in utf-8
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with requests.get(url) as res:
            res.raise_for_status()
            print(res.text)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))
