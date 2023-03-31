#!/usr/bin/python3
"""
This module provides a script that posts an email to url and
output the response contents
"""
import urllib.request as request
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    url, email = sys.argv[1:]
    data = urlencode({"email": email}).encode("ascii")

    with request.urlopen(url, data=data) as res:
        print(res.read1().decode("utf-8"))
