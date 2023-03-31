#!/bin/bash
# Post json content from file
curl -s -H "Content-Type: application/json" -H "Accept: application/json" -d @"$2" "$1"
