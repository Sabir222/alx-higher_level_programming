#!/usr/bin/python3
"""n."""


def read_file(filename=""):
    """P"""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
