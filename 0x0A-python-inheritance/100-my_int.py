#!/usr/bin/python3
"""ds"""


class MyInt(int):
    """ds"""
    def __eq__(self, other):
        """ds"""
        return int(self) != int(other)

    def __ne__(self, other):
        """ds"""
        return int(self) == int(other)
