#!/usr/bin/python3
'''modules.'''


class Base:
    '''Class Represent A Base.'''
    
    _nb_objects = 0

    def __init__(self, id = None):
        '''constructor'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
