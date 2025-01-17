#!/usr/bin/python3
"""takes in a URL, sends a request to the URL
    and displays the value
    of the variable X-Request-Id"""
import requests
import sys

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        response = requests.get(sys.argv[1])
        print(response.headers["X-Request-Id"])
    except Exception:
        pass
