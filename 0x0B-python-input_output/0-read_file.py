#!/usr/bin/python3
"""Define a functioo that reads."""



def read_file(filename=""):
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')i

if __name__ == "__main__":
    read_file("my_file_0.txt")
