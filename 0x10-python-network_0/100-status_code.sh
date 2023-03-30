#!/bin/bash
# Get status code using curl
curl -sL -w '%{http_code}' "$1" -o /dev/null
