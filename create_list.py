import os

from colorama import Fore as CA

# ---------------------------- PREPARATION ---------------------------------
# Set output filename
output_filename = "output-filename"
if not os.path.splitext(os.path.basename(output_filename))[1]:
    output_filename = output_filename + ".txt"

# Enter the extension of the files you want to search for
ext_of_files_searched = ".wav"

# Check true if in quotation marks
quotation_marks = True

# The input directory or .txt file with directories to search for files
input_dir = r"\\path\to\input.txt"
if os.path.splitext(os.path.basename(input_dir))[1] == ".txt":
    f = open(input_dir, "r")
    input_dir = f.read().split("\n")
else:
    input_dir = [input_dir]

# The output directory where the unpacked files will be saved
output_dir = r"\\path\to\output\directory"

# ---------------------------- PROCESSING ----------------------------------
found_files = []
for _, directory in enumerate(input_dir):
    print(CA.GREEN + f"[INFO] Working with {directory} ...")
    for file in os.listdir(directory):
        if file.endswith(ext_of_files_searched):
            abs_path = os.path.join(directory, file)
            if quotation_marks:
                abs_path = '''"''' + abs_path + '''"'''
            found_files.append(abs_path)

final_output_path = os.path.join(output_dir, output_filename)
print(CA.GREEN + f"[INFO] Save files to {final_output_path} ...")
output_file = open(final_output_path, 'w')
for file in found_files:
    output_file.write("\n" + file)
output_file.close()
