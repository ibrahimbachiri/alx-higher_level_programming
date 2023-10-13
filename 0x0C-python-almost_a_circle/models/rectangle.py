#!/usr/bin/python3
'''module Rectangle class.'''
from models.base import Base


class Rectangle(Base):
    '''A Rectangle class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''constructor.'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        '''height Rectangle.'''
        return self.__height = value

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        '''x Rectangle.'''
        return self. __x
    
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        '''y of Rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
