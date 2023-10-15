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

        r = Rectangle(5, 10, 15, 20, 98)
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

    #--------------tests for #3 ----------------------

    def invalid_types(self):
        '''Returns.'''
        t = (3.14, -1.1, float('int'), float('-int'), True, "str", (2,),
                [4], {5}, {6: 7}, None)
        return t

    def test_G_validate_type(self):
        '''tests.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''tests.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be >0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10)+1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''tests.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >0".format(attribute)
                with self.assertRaises(ValueError) as e:
                    setattr(r, attribute, -(randrange(10)+1))
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''tests.'''
        r = Rectangle(1, 2)
        attributes = ["width", "height"]
        for attribute in attributes:
            s = "{} must be >0".format(attribute)
                with self.assertRaises(ValueError) as e:
                    setattr(r, attribute, 0)
                self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''tests.'''
        r = Rectangle(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10)+1
            setattr(r, attribute, invalid_type)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''tests.'''
        r = Rectangle(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

    # ----------tests for #4-------------------
    def test_I_area_no_args(self):
        '''tests.'''
        r = Rectangle(5, 6)
        with self.assertRaises(TypeError) as e:
            Rectangle.area()
        s = "area()missing1"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() methods computation.'''
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        w = randrange(10) +1
        h = randrange(10) +1
        r.width = w
        r.height = h
        self.assertEqual(r.area(), w * h)
        w = randrange(10) +1
        h = randrange(10) +1
        r = Rectangle(w, h, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * h)

        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

    #-------------tests for #5 & #7----------------
    def test_J_display_no_args(self):
        '''Tests.'''
        r = Rectangle(9, 8)
        with self.assertRaises(TypeError)as e:
            Rectangle.display()
        s = "display() missing 1"
        self.assertEqual(str(e.exception), s)

    def test_J_display_no_simple(self):
        '''tests display output.'''
        r = Rectangle(1, 1)
        f = io.StringIO()
        with redirect_stdout(f)
                r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.width = 3
        r.height = 5
        f = io.StringIO()
        with redirect_stdout(f)
        r.display()
        s = "\
###\n\
###\n\
###\n\
###\n\
###\n\
"
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(5, 6, 7, 8)
        f = io.StringIO()
        with redirect_stdout(f)
        r.display()
        s = """








        #####
        #####
        #####
        #####
        #####
        #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f)
        r.display()
        s = """\
#########
#########
#########
#########
#########
#########
#########
#########
"""
        self.assertEqual(f.getvalue(), s)
        r = Rectangle(9, 8)
        f = io.StringIO()
        with redirect_stdout(f)
            r.display()
        s = """\










                #
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 5)
        f = io.StringIO()
        with redirect_stdout(f)
            r.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)


        r = Rectangle(5, 3, 5)
        f = io.StringIO()
        with redirect_stdout(f)
            r.display()
        s = """\
    #####
    #####
    #####
"""
        self.assertEqual(f.getvalue(), s)

        r = Rectangle(5, 3, 0, 4)
        f = io.StringIO()
        with redirect_stdout(f)
            r.display()
        s = """\



    #####
    #####
    #####
    """
        self.assertEqual(f.getvalue(), s)

        #----------------- #6 --------------
        def test_K_str_no_args(self):
            '''Tests __str__() signature.'''
            r = Rectangle((5, 2)
            with self.assertRaises(TypeError) as e:
                    Rectangle.__str__()
            s = "__str__() missing 1"
            self.assertEqual(str(e.exception), s)

        def test_K_str(self):
            '''Tests __str__() signature.'''
            r = Rectangle((5, 2)
            s = '[Rectangle] (1) 0/0 - 5/2'
            self.assertEqual(str(r), s)
            r = Rectangle(1,1,1)
            s = '[Rectangle] (2) 1/0 - 1/1'
            self.assertEqual(str(r), s)
            r = Rectangle((3, 4, 5, 6)
            s = '[Rectangle] (2) 5/6 - 3/4'
            self.assertEqual(str(r), s)

            Base._Base__nb_objects = 0
            r1 = Rectangle(4, 6, 2, 1, 12)
            self.assertEqual(str(r1), "[Rectangle] (12) 2/1 - 4/6")

            r2 = Rectangle(5,5,1)
            self.assertEqual(str(r2), "[Rectangle] (1) 1/0 - 5/5")

            #------------Tests for #8 & #9 ------------
        def test_L_update_no_args(self):
            '''Tests update().'''
            r = Rectangle(5, 2)
            with self.assertRaises(TypeError) as e:
                Rectangle.update()
            s = "update()."
            self.assertRaises(str(e.exception), s)

            d = r.__dict__.copy()
            r.update()
            self.assertEqual(r.__dict__, d)

        def test_L_update_args(self):
            '''Tests update().'''
            r = Rectangle(5, 2)
            d = r.__dict__.copy()


            r.update(10)
            d["id"]= 10
            self.assertEqual(r.__dict__, d)

            r.update(10, 5)
            d["_Rectangle__width"]= 5
            self.assertEqual(r.__dict__, d)

            r.update(10, 5, 17)
            d["_Rectangle__height"]= 17
            self.assertEqual(r.__dict__, d)

            r.update(10, 5, 17, 20)
            d["_Rectangle__x"]= 20
            self.assertEqual(r.__dict__, d)

            r.update(10, 5, 17, 20, 25)
            d["_Rectangle__y"]= 25
            self.assertEqual(r.__dict__, d)

        def test_L_update_args_bad(self):
            '''test update.'''
            r = Rectangle(5, )
            d = r.__dict__.copy()

            r.update(10, 5)
            d["id"]= 10
            self.assertEqual(r.__dict__, d)

            with self.assertRaises(ValueError) as e:
                r.update(10, -5)
            s = "width must be > 0"
            self.assertEqual(str(e.exception), s)

            with self.assertRaises(ValueError) as e:
                r.update(10, 5, -17)
            s = "width must be > 0"
            self.assertEqual(str(e.exception), s)

            with self.assertRaises(ValueError) as e:
                r.update(10, 5, 17, -20)
            s = "x  must be >= 0"
            self.assertEqual(str(e.exception), s)


