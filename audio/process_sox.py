import os
import sox

from colorama import Fore as CA

# ---------------------------- DESCRIPTION ---------------------------------
# Please note that to use SoX in Python and therefore this script, you must
# have the SoX package installed: https://sourceforge.net/projects/sox/

# ---------------------------- PREPARATION ---------------------------------
# The input directory or .txt file with directories where the files to be
# processed are located
input_dir = r"\\path\to\input.txt"
if os.path.splitext(os.path.basename(input_dir))[1] == ".txt":
    f = open(input_dir, "r")
    input_dir = f.read().split("\n")
else:
    input_dir = [input_dir]

# The output directory where the processed files will be saved
output_dir = r"\\path\to\output"

# Input file preparation
input_file_type = "raw"
input_fs = 16000
input_bits = 16
input_encoding = "signed-integer"
input_channels = 1

# Output file preparation
output_file_type = "wav"
output_fs = None
output_bits = None
output_encoding = None
output_channels = None

# ---------------------------- PROCESSING ----------------------------------
tfm = sox.Transformer()
tfm.set_input_format(
    file_type=input_file_type,
    rate=input_fs,
    bits=input_bits,
    encoding=input_encoding,
    channels=input_channels,
)
tfm.set_output_format(
    file_type=output_file_type,
    rate=output_fs,
    bits=output_bits,
    encoding=output_encoding,
    channels=output_channels,
)

for _, directory in enumerate(input_dir):
    final_output_dir = os.path.join(
        output_dir, os.path.splitext(os.path.basename(directory))[0]
    )
    if not os.path.isdir(final_output_dir):
        os.mkdir(final_output_dir)
    number_of_file_to_processing = len(os.listdir(directory))
    print(CA.GREEN + f"[INFO] Working with {directory} ...")
    for i, file in enumerate(os.listdir(directory)):
        print(
            CA.GREEN
            + f"[INFO] Processing {i + 1} of {number_of_file_to_processing}..."
        )
        if "_" not in file:
            split_name = os.path.splitext(os.path.basename(file))
            output_filename = (
                split_name[0] + split_name[1].replace(".", "_") + ".wav"
            )
            processed_file = os.path.join(directory, file)
            output_path = os.path.join(final_output_dir, output_filename)
            tfm.build_file(
                input_filepath=processed_file, output_filepath=output_path
            )
