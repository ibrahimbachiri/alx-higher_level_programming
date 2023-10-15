#!/usr/bin/python3
'''modules.'''
import unittest
from models.base import base
from models.rectangle import Rectangle
from random import randrange
from contetlib import redirect_stdout
import io


class TestRectangle(unittest.TestCase):
    '''the class.'''

    def setUp(self):
        '''imports.'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''cleans.'''
        pass

    # ---------Tests for #2------------------

    def test_A_class(self):
        '''Tests Rectangle.'''
        self.assertEqual(str(Rectangle),
                "<class 'models.rectangle.Rectangle'>")

    def test_B_inheritance(self):
        '''Rectangle.'''
        self.assertTrue(issubclass(Rectangle, Base))

    def test_C_contructor_no_args(self):
        '''constrctor.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle()
        s = "__init__() missing 2 required positional argument :width \
                and 'height'"
        self.assertEqual(str(e.excepion), s)

    def test_C_constructor_many_args(self):
        '''signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, 4, 5, 6)
        s = "__init__()"

        self.assertEqual(str(e.exception), s)

    def test_C_constructor_one_args(self):
        '''signature.'''
        with self.assertRaises(TypeError) as e:
            r = Rectangle(1)
        s = "__init__() missing 1"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''instantiation.'''
        r = Rectangle(10, 20)
        self.assertEqual(str(type(r)), "<class 'module'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 20, '_Rectangle__width':10,
                '_Rectangle__x': 0, '_Rectangle__y':0, 'id':1}
        self.assertDictEqual(r.__dict__,d)

        with self.assertRaises(TypeError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

       with self.assertRaises(TypeError) as e:
            r = Rectangle(1, "2")
        msg = "height must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, "3")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, 2, 3, "4")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(-1, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Rectangle(1, -2)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(0, 2)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 0)
        msg = "height must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle("1", 2)
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, -3)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Rectangle(1, 2, 3, -4)
        msg = "y must be >= 0 "
        self.assertEqual(str(e.00exception), msg)

    def test_D_instantiation_positional(self):
        '''tests.'''
        r = Rectangle(5, 10, 15, 20)
        d = {'_Rectangle__height': 10, '_Rectangle__width': 5,
                '_Rectangle__x':15, '_Rectangle__y': 20, 'id': 1}
        self.assertEqual(r.__dict__, d)


