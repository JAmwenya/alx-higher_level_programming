#!/usr/bin/python3
"""This module defines a funtion that converts an object to JSON."""
import json


def to_json_string(my_obj):
    """
    Function that converts an object to its JSON representation.

    Args:
        my_obj: The object to be converted to JSON.

    Returns:
        str: The JSON representation of the object.
    """
    return json.dumps(my_obj)
