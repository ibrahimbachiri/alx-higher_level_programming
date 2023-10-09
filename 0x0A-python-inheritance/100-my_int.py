#!/usr/bin/python3

class MyInt(int):
    def __init__(self, value):
        super().__init__()
        self.value = value


def __eq__(self, other):
        return self.value != other

def __ne__(self, other):
        return self.value == other                                                
