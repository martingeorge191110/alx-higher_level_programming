#!/usr/bin/python3
"""Python script that list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    try:
        url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[1], sys.argv[2]
        )

        response = requests.get(url)
        commits = response.json()

        for i in range(10):
            sha = commits[i].get("sha")
            name = commits[i].get("commit").get("author").get("name")
            print(f"{sha}: {name}")
    except Exception:
        pass
