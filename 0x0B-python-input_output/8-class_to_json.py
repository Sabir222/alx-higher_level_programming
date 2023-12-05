#!/usr/bin/python3
"""
fin
"""


def class_to_json(obj):
    """ ucture """

    structure = {}
    if hasattr(obj, "__dict__"):
        structure = obj.__dict__.copy()
    return structure
