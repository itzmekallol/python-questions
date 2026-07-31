"""
Q17: A plugin system that dynamically discovers, loads, and executes
plugin modules from the "plugins" package using importlib.

Run with: python main.py
"""

import importlib
import os
import pkgutil

import plugins  # the plugins package sitting next to this file


def discover_plugins(package):
    """
    Scans the given package for modules and dynamically imports each
    one using importlib, returning them as a dict of name -> module.
    """
    discovered = {}
    package_path = package.__path__
    for _, module_name, is_pkg in pkgutil.iter_modules(package_path):
        if is_pkg:
            continue
        full_module_name = f"{package.__name__}.{module_name}"
        module = importlib.import_module(full_module_name)
        if hasattr(module, "PLUGIN_NAME") and hasattr(module, "run"):
            discovered[module.PLUGIN_NAME] = module
    return discovered


def main():
    print("Q17: Dynamic plugin system")

    loaded_plugins = discover_plugins(plugins)
    print("Discovered plugins:", list(loaded_plugins.keys()))

    sample_text = "Python makes dynamic plugin loading straightforward"
    print(f"\nRunning every plugin on: '{sample_text}'")
    for plugin_name, plugin_module in loaded_plugins.items():
        result = plugin_module.run(sample_text)
        print(f"[{plugin_name}] -> {result}")


if __name__ == "__main__":
    main()
