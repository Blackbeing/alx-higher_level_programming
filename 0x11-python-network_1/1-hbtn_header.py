#!/usr/bin/python3
"""
This module provides a script that takes url argument, fetches url
and displays contest of X-Request-Id variable
"""

import urllib.request as request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as res:
        print(res.getheader("X-Request-Id"))
