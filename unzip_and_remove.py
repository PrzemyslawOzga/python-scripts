import os
import zipfile
from colorama import Fore as ca

"""
A script that searches for files with the .zip and .7z extensions
with the maximum single nesting degree and unpacks them in the
same folder.
"""

current_dir = r"path/to/working/directory"
if not os.path.exists(current_dir):
    raise ValueError(ca.RED + f"[ERROR] File {current_dir} do not exist.")

for item in os.listdir(current_dir):
    path_to_item = os.path.join(current_dir, item)
    print(ca.GREEN + f"[INFO] Working with {item} ...")
    if not os.path.isfile(path_to_item):
        for file in os.listdir(path_to_item):
            if file.endswith(".zip") or file.endswith(".7z"):
                file_name, _ = os.path.splitext(file)
                output_dir = os.path.join(path_to_item, file_name)
                os.mkdir(output_dir)
                file_to_unzip = os.path.join(path_to_item, file)
                try:
                    with zipfile.ZipFile(file_to_unzip, 'r') as zip_ref:
                        zip_ref.extractall(output_dir)
                    print(ca.GREEN + f"[INFO] Unzip {file_to_unzip} done.")
                except ValueError:
                    print(ca.YELLOW + f"[WARNING] Unzip {file_to_unzip} unsuccessful.")
                    continue
                try:
                    os.remove(file_to_unzip)
                    print(ca.GREEN + f"[INFO] Rmdir {file_to_unzip} done.")
                except OSError:
                    print(ca.YELLOW + f"[WARNING] Rmdir {file_to_unzip} unsuccessful.")
                    continue
    print(ca.GREEN + f"[INFO] Working with {item} done.\n")
