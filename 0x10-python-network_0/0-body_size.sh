#!/bin/bash
# Takes in a URL, sends a request to that URL, then displays the length of the body of the response
curl -s "$1" | wc -c
