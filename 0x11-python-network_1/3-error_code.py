#!/usr/bin/python3
"""Takes in a URL,
    sends a request to the URL
    and displays the body of the response"""
from urllib import request, error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as resp:
            print(resp.read().decode("utf-8"))
    except error.HTTPError as err:
        print("Error code: {}".format(err.code))
