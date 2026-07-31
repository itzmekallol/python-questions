"""
plugin_uppercase.py — a plugin that converts text to uppercase.

Every plugin module in this package exposes a PLUGIN_NAME and a
run(text) function, which is the "contract" the plugin loader expects.
"""

PLUGIN_NAME = "Uppercase Converter"


def run(text):
    return text.upper()
