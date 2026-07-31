"""
plugin_word_count.py — a plugin that counts words in text.
"""

PLUGIN_NAME = "Word Counter"


def run(text):
    return f"{len(text.split())} word(s)"
