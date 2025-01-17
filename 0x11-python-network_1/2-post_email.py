#!/usr/bin/python3
"""sends a POST request to the passed URL with
    the email as a parameter,
    and displays the body of
    the response (decoded in utf-8)"""
from urllib import request, parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    req = request.Request(url,
                        parse.urlencode({"email", email}).encode("asci"))
    with request.urlopen(req) as resp:
        print(resp.read().decode("utf-8"))
