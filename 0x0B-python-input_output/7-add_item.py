#!/usr/bin/python3
""""""


import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    listItems = load_from_json_file("add_item.json")
except FileNotFoundError:
    listItems = []
listItems.extend(sys.argv[1:])
save_to_json_file(listItems, "add_item.json")
