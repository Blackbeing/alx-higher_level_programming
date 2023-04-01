#!/usr/bin/python3
"""
This module provides a script that queries the Github API and prints
10 commits from repo by user
"""
import requests
import sys

if __name__ == "__main__":
    repo, owner = sys.argv[1:]
    query = {"per_page": 10}

    req = requests.get(
        "https://api.github.com/repos/{}/{}/commits".format(owner, repo),
        params=query,
    )
    for _ in req.json():
        print(
            "{}: {}".format(
                _.get("sha"),
                _.get("commit", {}).get("author", {}).get("name", ""),
            )
        )
