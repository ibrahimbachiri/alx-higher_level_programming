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
        r = Square(100, id=421, y=99, x=101)
        d = {'_Rectangle__height': 200, '_Rectangle__width': 100,
                '_Rectangle__x':101, '_Rectangle__y': 99, 'id': 421}
        self.assertEqual(r.__dict__, d)

    def test_E_id_inherited(self):
        '''Tests.'''
        Base.Base_nb_objects = 98
        r = Square(2)
        self.assertEqual(r.id, 99)

    def test_F_properties(self):
        '''tests.'''
        r = Square(5, 9)
        r.size = 98
        r.x = 102
        r.y = 103
        d = {'_Rectangle__height': 101, '_Rectangle__width':100,
                '_Rectanle__x': 102, '_Rectangle__y': 103, 'id':1}
        self.assertEqual(r.__dict__, d)
        self.assertEqual(r.size, 98)
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
        r = Square(1)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be an integer".format(attribute)
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)
        s = "{} must be an integer"
            for invalid_type in self.invalid_types():
                with self.assertRaises(TypeError) as e:
                    setattr(r, attribute, invalid_type)
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_gt(self):
        '''tests.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "{} must be >0".format(attribute)
            with self.assertRaises(ValueError) as e:
                setattr(r, attribute, -(randrange(10)+1))
            self.assertEqual(str(e.exception), s)

    def test_G_validate_value_negative_ge(self):
        '''tests.'''
        r = Square(1, 2)
        attributes = ["x", "y"]
        for attribute in attributes:
            s = "{} must be >0".format(attribute)
                with self.assertRaises(ValueError) as e:
                    setattr(r, attribute, -(randrange(10)+1))
                self.assertEqual(str(e.exception), s)

    def test_G_validate_value_zero(self):
        '''tests.'''
        r = Square(1, 2)
        attributes = ["size"]
        for attribute in attributes:
            s = "{} must be >0".format(attribute)
                with self.assertRaises(ValueError) as e:
                    setattr(r, attribute, 0)
                self.assertEqual(str(e.exception), s)

    def test_H_property(self):
        '''tests.'''
        r = Square(1, 2)
        attributes = ["x", "y", "width", "height"]
        for attribute in attributes:
            n = randrange(10) + 1
            setattr(r, attribute, n)
            self.assertEqual(getattr(r, attribute), n)

    def test_H_property_range_zero(self):
        '''tests.'''
        r = Square(1, 2)
        r.x = 0
        r.y = 0
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)

        # ----------tests for #4-------------------
        def test_I_area_no_args(self):
        '''tests.'''
        r = Square(5)
        with self.assertRaises(TypeError) as e:
            Square.area()
        s = "area()missing1"
        self.assertEqual(str(e.exception), s)

    def test_I_area(self):
        '''Tests area() methods computation.'''
        r = Square(6)
        self.assertEqual(r.area(), 36)
        w = randrange(10) +1
        r.size = w
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, 7, 8, 9)
        self.assertEqual(r.area(), w * w)
        w = randrange(10) + 1
        r = Square(w, y=7, x=8, id=9)
        self.assertEqual(r.area(), w * w)

        Base._Base_nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[area](1), 6")
        self.assertEqual(s1.size, 5)
        s1.size = 10
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 6")
        self.assertEqual(s1.size, 10)

        with self.assertRaises(TypeError) as e:
            s1.size = "g"
        self.assertEqual(str(e.exception), "width"

        with self.assertRaises(ValueError) as e:
            s1.size = 0
        self.assertEqual(str(e.exception), "width" )

        #-------------tests for #5 & #7----------------
    def test_J_display_no_args(self):
        '''Tests.'''
        r = Square(9)
        with self.assertRaises(TypeError)as e:
            Square.display()
        s = "display() missing 1"
        self.assertEqual(str(e.exception), s)

    def test_J_display_no_simple(self):
        '''tests display output.'''
        r = Square(1)
        f = io.StringIO()
        with redirect_stdout(f)
                r.display()
        s = "#\n"
        self.assertEqual(f.getvalue(), s)
        r.size = 3
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
        r = Square(5, 6, 7)
        f = io.StringIO()
        with redirect_stdout(f)
        r.display()
        s = """\








        #####
        #####
        #####
        #####
        #####
        #####
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(9, 8)
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
        #########
"""
        self.assertEqual(f.getvalue(), s)
        r = Square(1, 1, 10)
        f = io.StringIO()
        with redirect_stdout(f)
            r.display()
        s = """\










                #
"""
        self.assertEqual(f.getvalue(), s)

        r = Square(5, 5)
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


        r = Square(5, 3)
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

        r = Square(5, 0, 4)
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

        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s1.area(), 25)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
#####
#####
#####
#####
#####
"""
        self.assertEqual(f.getvalue(), s)

        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s2.area(), 4)
        f = io.StringIO()
        with redirect_stdout(f):
            s1.display()
        s = """\
##
##
"""
         self.assertEqual(f.getvalue(), s)

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 5")
        self.assertEqual(s3.area(), 9)
        f = io.StringIO()
        with redirect_stdout(f):
            s3.display()
        s = """\



###
###
###
"""
        self.assertEqual(f.getvalue(), s)

        #----------------- #6 --------------
        def test_K_str_no_args(self):
            '''Tests __str__() signature.'''
            r = Square((5, 2)
            with self.assertRaises(TypeError) as e:
                    Square.__str__()
            s = "__str__() missing 1"
            self.assertEqual(str(e.exception), s)

        def test_K_str(self):
            '''Tests __str__() signature.'''
            r = Square((5)
            s = '[Rectangle] (1) 0/0 - 5/2'
            self.assertEqual(str(r), s)
            r = Square(1,1)
            s = '[Square] (2) 1/0 - 1/1'
            self.assertEqual(str(r), s)
            r = Square(3, 4, 5)
            s = '[Rectangle] (2) 5/6 - 3/4'
            self.assertEqual(str(r), s)
            r = Square(10, 20, 30, 40)
            s = '[Square] (40) 20/30 - 10'
            self.assertEqual(str(r), s)

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

            with self.assertRaises(ValueError) as e:
                r.update(10, -5)
            s = "y must be >= 0"
            self.assertEqual(str(e.exception), s)

    def test_L_update_kwargs(self):
            '''test update.'''
            r = Rectangle(5, 2)
            d = r.__dict__.copy()

            r.update(id=10)
            d["id"]= 10
            self.assertEqual(r.__dict__, d)

            r.update(width=5)
            d["_Rectangle_width"]= 5
            self.assertEqual(r.__dict__, d)

            r.update(height=17)
            d["_Rectangle_width"]= 17
            self.assertEqual(r.__dict__, d)

            r.update(x=20)
            d["_Rectangle_x"]= 20
            self.assertEqual(r.__dict__, d)

            r.update(y=25)
            d["_Rectangle_y"]= 25
            self.assertEqual(r.__dict__, d)

     def test_L_update_kwargs_2(self):
            '''test update.'''
            r = Rectangle(5, 2)
            d = r.__dict__.copy()

            r.update(id=10)
            d["id"]= 10
            self.assertEqual(r.__dict__, d)

            r.update(id=10, width=5)
            d["_Rectangle__width"]= 5
            self.assertEqual(r.__dict__, d)

            r.update(id=10, width=5, height=17)
            d["_Rectangle__width"]= 17
            self.assertEqual(r.__dict__, d)

            r.update(id=10, width=5, height=17, x=20)
            d["_Rectangle__x"]= 20
            self.assertEqual(r.__dict__, d)

            r.update(id=10, width=5, height=17, x=20, y=25)
            d["_Rectangle__x"]= 25
            self.assertEqual(r.__dict__, d)

            r.update(y=25, id=10, height=17, x=20, width=5)
            self.assertEqual(r.__dict__, d)

            Base._Base__nb_objects = 0
            r1 = Rectnagle(10, 10, 10, 10)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10")

            r1.update(height=1)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/1")

            r1.update(width=1, x=2)
            self.assertEqual(str(r1), "[Rectangle] (1) 2/10 - 1/1")

            r1.update(y=1,width=2, x=3, id=89)
            self.assertEqual(str(r1), "[Rectangle] (89) 3/1 2/1")

            r1.update(x=1, height=2, y=3, width=4)
            self.assertEqual(str(r1), "[Rectangle] (89) 1/3 - 4/2")

            Base._Base__nb_objects = 0
            r1 = Rectnagle(10, 10, 10, 10)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10 -10/10")

            r1.update(89)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10 -10/10")

            r1.update(89, 2)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10 -2/10")

            r1.update(89, 2, 3)
            self.assertEqual(str(r1), "[Rectangle] (1) 10/10 -2/3")

            r1.update(89, 2, 3, 4)
            self.assertEqual(str(r1), "[Rectangle] (89) 4/5 - 2/3")
