"""
Q9: Configuration loader. Reads settings from a JSON file, supplies
default values for missing keys, and handles invalid JSON gracefully.

Run with: python main.py
"""

import json
import os

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "practice_files")
os.makedirs(DATA_DIR, exist_ok=True)


def path(filename):
    return os.path.join(DATA_DIR, filename)


DEFAULT_CONFIG = {
    "app_name": "MyApp",
    "debug": False,
    "max_connections": 10,
    "timeout_seconds": 30,
}


class ConfigLoader:
    def __init__(self, filename, defaults=None):
        self.filename = filename
        self.defaults = defaults or {}
        self.config = self._load()

    def _load(self):
        if not os.path.exists(self.filename):
            print(f"Config file '{self.filename}' not found; using all defaults")
            return dict(self.defaults)

        try:
            with open(self.filename, "r") as f:
                loaded = json.load(f)
        except json.JSONDecodeError:
            print(f"Warning: '{self.filename}' contains invalid JSON; using all defaults")
            return dict(self.defaults)

        # merge: values from the file override defaults, missing keys fall back
        merged = dict(self.defaults)
        merged.update(loaded)
        return merged

    def get(self, key):
        return self.config.get(key, self.defaults.get(key))


def main():
    print("Q9: Configuration loader")

    # Case 1: a valid but incomplete config file (missing max_connections/timeout_seconds)
    partial_config_file = path("partial_config.json")
    with open(partial_config_file, "w") as f:
        json.dump({"app_name": "InventoryTracker", "debug": True}, f)

    loader1 = ConfigLoader(partial_config_file, DEFAULT_CONFIG)
    print("\nPartial config loaded (missing keys filled with defaults):")
    print(loader1.config)

    # Case 2: an invalid JSON file
    invalid_config_file = path("invalid_config.json")
    with open(invalid_config_file, "w") as f:
        f.write("{ this is not valid json, }")

    loader2 = ConfigLoader(invalid_config_file, DEFAULT_CONFIG)
    print("\nInvalid JSON config (falls back to all defaults):")
    print(loader2.config)

    # Case 3: a missing file entirely
    loader3 = ConfigLoader(path("does_not_exist.json"), DEFAULT_CONFIG)
    print("\nMissing config file (falls back to all defaults):")
    print(loader3.config)


if __name__ == "__main__":
    main()
