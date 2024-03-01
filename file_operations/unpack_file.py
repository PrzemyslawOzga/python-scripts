import os
import zipfile

from colorama import Fore as CA

# ---------------------------- PREPARATION --------------------------------- NEW
# Check the flag to true if the file is to be deleted after unpacking
remove_after_unpacking = False

# The input directory or .txt file with directories where the files to be
# unpacked are located
input_dir = r"\\path\to\input.txt"
if os.path.splitext(os.path.basename(input_dir))[1] == ".txt":
    f = open(input_dir, "r")
    input_dir = f.read().split("\n")
else:
    input_dir = [input_dir]

# The output directory where the unpacked files will be saved
output_dir = r"\\path\to\output"

# ---------------------------- PROCESSING ----------------------------------
for _, directory in enumerate(input_dir):
    print(CA.GREEN + f"[INFO] Working with {directory}...")
    for file in os.listdir(directory):
        if file.endswith(".zip") or file.endswith(".7z"):
            file_name, _ = os.path.splitext(file)
            output_dir = os.path.join(output_dir, file_name)
            if not os.path.isdir(output_dir):
                os.mkdir(output_dir)
            file_to_unzip = os.path.join(directory, file)
            try:
                with zipfile.ZipFile(file_to_unzip, "r") as zip_ref:
                    zip_ref.extractall(output_dir)
                print(CA.GREEN + f"[INFO] Unzip {file_to_unzip} done.")
            except ValueError:
                print(CA.YELLOW + f"[WARNING] Unzip {file_to_unzip} unsuccessful.")
                decision = input(CA.YELLOW + "[WARNING] Press Y if you want to continue...")
                if decision == "Y":
                    continue
                else:
                    break
            if remove_after_unpacking:
                try:
                    os.remove(file_to_unzip)
                    print(CA.GREEN + f"[INFO] Rmdir {file_to_unzip} done.")
                except OSError:
                    print(CA.YELLOW + f"[WARNING] Rmdir {file_to_unzip} unsuccessful.")
                    decision = input(CA.YELLOW + "[WARNING] Press Y if you want to continue...")
                    if decision == "Y":
                        continue
                    else:
                        break
