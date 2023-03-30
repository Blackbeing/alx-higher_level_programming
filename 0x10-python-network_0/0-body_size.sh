#!/bin/bash
# Display the size of the body of response
curl -s -w '%{size_download}\n' "$1" -o /dev/null
