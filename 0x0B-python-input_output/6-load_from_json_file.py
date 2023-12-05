#!/usr/bin/python3
"""ction."""
import json


def load_from_json_file(filename):
    """N file."""
    with open(filename) as f:
        return json.load(f)
