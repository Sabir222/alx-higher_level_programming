#!/usr/bin/python3
"""ds"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ds"""
    def __init__(self, size):
        """ds"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """ds"""
        return self.__size ** 2

    def __str__(self):
        """ds"""
        return "[Square] {}/{}".format(self.__size, self.__size)
