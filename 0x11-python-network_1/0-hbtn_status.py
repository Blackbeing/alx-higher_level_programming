#!/usr/bin/python3
"""
This module provides a script that fetches url and output its contents
"""
import urllib.request as request

if __name__ == "__main__":
    with request.urlopen("https://alx-intranet.hbtn.io/status") as res:
        print("Body response:")
        content = res.read1()
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode("utf-8")))
