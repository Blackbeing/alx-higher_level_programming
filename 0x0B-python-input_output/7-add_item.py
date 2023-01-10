#!/usr/bin/python3
"""
This modules takes cmd args, appends to list, writes to json file
"""
import sys
import json
from pathlib import Path

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file_name = "add_item.json"

try:
    current_list = load_from_json_file(file_name)
except FileNotFoundError:
    Path(file_name).touch()
    current_list = []
except json.decoder.JSONDecodeError:
    current_list = []

cmd_args = sys.argv[1:]
current_list.extend(cmd_args)

save_to_json_file(current_list, file_name)
