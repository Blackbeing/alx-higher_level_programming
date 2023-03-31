#!/usr/bin/python3
"""
This module provides a script that takes in url as argument, sends a
request and prints body of response decoded in utf-8
"""
import urllib.request as request
import urllib.error as error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as res:
            print(res.read1().decode("utf-8"))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
