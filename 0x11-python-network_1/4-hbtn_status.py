#!/usr/bin/python3
"""
This module provides a script that fetches url and prints
its content and content type
"""
import requests

res = requests.get("https://alx-intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(res.text)))
print("\t- content: {}".format(res.text))
