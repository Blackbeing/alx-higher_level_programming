#!/usr/bin/python3
"""
This module provides a script that posts an email to url and
output the response contents
"""
import requests
import sys

if __name__ == "__main__":
    url, email = sys.argv[1:]
    data = {"email": email}
    res = requests.post(url, data=data)
    print(res.text)
