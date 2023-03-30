#!/bin/bash
# Get Allowed http methods
 curl -si "$1"  | grep Allow: | cut -d' ' -f2-
