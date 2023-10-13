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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs:
            '''jsonified object to file.'''
            if list_objs is not None:
                list_objs = [o.to_dictionary() for o in list_objs]
            with open("{}.json".format(cls.__name__),"w", encoding="utf-8")as f:


