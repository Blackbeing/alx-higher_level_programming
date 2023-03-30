#!/bin/bash
# Send get request and display response, add header
curl -sL -H "X-School-User-Id: 98" "$1"
