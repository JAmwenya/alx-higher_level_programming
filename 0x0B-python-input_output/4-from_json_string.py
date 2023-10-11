#!/usr/bin/python3
"""A module that defines a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """
    A function that returns an object (Python data structure) represented by a JSON string

    Args:
        my_str: The JSON string to be parsed.

    Returns:
        object: The Python data structure (object) represented by the JSON string.
    """
	return json.loads(my_str)
