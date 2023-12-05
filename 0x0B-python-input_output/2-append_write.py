#!/usr/bin/python3
"""tion."""


def append_write(filename="", text=""):
    """Aded.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
