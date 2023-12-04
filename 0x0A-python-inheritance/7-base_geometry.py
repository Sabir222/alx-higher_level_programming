#!/usr/bin/python3
"""lol"""


class BaseGeometry:
    """lol"""

    def area(self):
        """lol"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """lol"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
