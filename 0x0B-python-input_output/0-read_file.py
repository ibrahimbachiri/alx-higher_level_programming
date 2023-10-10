#!/usr/bin/python3
"""Definition of afile."""


def read_file(filename=""):
        with open(filename, mode='r', encoding='utf-8') as file:
            for line in file:
                print(line, end='')

if __name__ == "__main__":
    read_file("my_file_0.txt")
