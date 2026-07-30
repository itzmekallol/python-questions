"""
file_utils.py — part of the utilities package.
"""

import os


def file_exists(filename):
    return os.path.exists(filename)


def get_file_size(filename):
    if os.path.exists(filename):
        return os.path.getsize(filename)
    return None


def create_text_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    return f"File '{filename}' created"
