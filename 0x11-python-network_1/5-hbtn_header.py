#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
    and displays the value
    of the variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        response = requests.get(url)
        print(response.headers["X-Request-Id"])
    except Exception:
        pass
