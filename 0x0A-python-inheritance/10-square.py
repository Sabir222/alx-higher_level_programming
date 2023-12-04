#!/usr/bin/python3
"""lol"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """lol"""
    def __init__(self, size):
        """lol"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """lol"""
        return self.__size ** 2
