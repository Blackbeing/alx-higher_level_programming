#!/bin/bash
# Send get request and display response, add header
curl -sL -d 'email=test@gmail.com' -d 'subject=I will always be here for PLD' "$1"
