#!/usr/bin/python3
""" Definition of a fle."""


def read_file(filename=""):
    with open(filename,'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
