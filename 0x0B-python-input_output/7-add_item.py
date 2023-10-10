#!/usr/bin/python3
"""module"""


import sys
save_to_json_file =___import__('5-save_to_json_file').save_to_json_file
load_from_json_file=__import__('6-load_from_json_file').load_from_json_file

arglist = list(says.argv[1:])

try:
    old_data= load_from_json_file('add_item.json')
except Exception:
    old_data = []

old_data.extend(arglist)
save_to_join_file(old_data,'add_item.json)
