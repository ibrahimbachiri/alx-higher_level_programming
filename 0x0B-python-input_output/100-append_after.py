#!/usr/bin/python3
"""contains the "append after" function"""

def append_after(filename="", search_string="", new_string=""):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    with open(filename, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
