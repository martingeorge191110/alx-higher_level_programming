#!/usr/bin/python3
# script that fetches https://alx-intranet.hbtn.io/status
import urllib.request

with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as resp:
    print("Body response:")
    print("\t- type: {}".format(type(resp.read())))
    print("\t- content: {}".format(resp.read()))
    print("\t- utf8 content: {}".format(resp.read().decode('utf-8')))
