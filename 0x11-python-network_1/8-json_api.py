#!/usr/bin/python3
""" takes in a letter and
    sends a POST request
    to http://0.0.0.0:5000/search_user
    with the letter as a parameter."""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    response = requests.post("http://0.0.0.0:5000/search_user", data={"q": q})
    try:
        json = response.json()
        if json:
            print("[{}] {}".format(json.get('id'), json.get('name')))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
