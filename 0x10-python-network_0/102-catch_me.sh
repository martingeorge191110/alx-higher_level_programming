#!/bin/bash
#  request to 0.0.0.0:5000/catch_me causes the server to respond with a message, in the response body
curl -sL -X PUT -H "Origin: School" -d "user_id=98" 0.0.0.0:5000/catch_me
