"""
q9_os_module_demo.py

Q9: Uses the os module to display the current working directory,
create a folder, rename it, and then delete it.
"""

import os

print("Q9: Built-in os module")

current_dir = os.getcwd()
print("Current working directory:", current_dir)

folder_name = "demo_folder"
renamed_folder = "demo_folder_renamed"

os.makedirs(folder_name, exist_ok=True)
print(f"Created folder: {folder_name}")

os.rename(folder_name, renamed_folder)
print(f"Renamed folder to: {renamed_folder}")

os.rmdir(renamed_folder)
print(f"Deleted folder: {renamed_folder}")
print("Folder still exists:", os.path.exists(renamed_folder))
