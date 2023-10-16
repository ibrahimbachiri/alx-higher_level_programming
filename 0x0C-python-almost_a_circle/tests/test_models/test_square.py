#!/usr/bin/python3
'''modules.'''
import unittest
from models.base import Base
from models.square import square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''the class.'''

    def setUp(self):
        '''imports.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''cleans.'''
        pass
    # ------------Test 2 ---------------------

    def test_A_class(self):
        '''Tests Rectangle.'''
        self.assertEqual(str(Square),
                "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Rectangle.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_contructor_no_args(self):
        '''constrctor.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 2 required positional argument :width \
                and 'height'"
        self.assertEqual(str(e.excepion), s)

    def test_C_constructor_many_args(self):
        '''signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__()"

        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''instantiation.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'module'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width':10,
                '_Rectangle__x': 0, '_Rectangle__y':0, 'id':1}
        self.assertDictEqual(r.__dict__,d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

       with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, -2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''tests.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                '_Rectangle__x':15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                '_Rectangle__x':15, '_Rectangle__y': 20, 'id': 98}
        self.assertEqual(r.__dict__, d)

    def test_D_instantiation_keyword(self):
        '''Tests.'''
        r = Rectangle(100, 200, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
                '_Rectangle__x':101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests.'''
        Base.Base_nb_objects = 98
        r = Rectangle(2, 4)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''tests.'''
        r = Rectangle(5, 9)
        r.width = 100
        r.height = 101
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width':100,
                '_Rectanle__x': 102, '_Rectangle__y': 103, 'id':1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.width, 100)
        self.assertEqual(r.height, 101)
        self.assertEqual(r.x, 102)
        self.assertEqual(r.y, 103)
