#!/usr/bin/python3
"""defining load_from_json_file"""


import json


def load_from_json_file(filename):
    """creates an object from json file"""
    with open(filename,"w", encoding="utf-8")as f:
        return json.load(f)
