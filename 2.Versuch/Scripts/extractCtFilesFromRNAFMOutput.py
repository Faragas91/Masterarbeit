import os
import shutil

input_dir = "D:/Masterarbeit/2.Versuch/Data/Result/RNA-FM/"
output_dir = "D:/Masterarbeit/2.Versuch/Data/Result/RNA-FM_CT/"

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

def extractCtFiles(input_dir, output_dir):
    for files in os.listdir(input_dir):
        for file in os.listdir(files):
            if file.endswith(".ct"):
                input_file = os.path.join(files, file)
                output_file = os.path.join(output_dir, file)
                shutil.copy(input_file, output_file)
                print(f"Copied {input_file} to {output_file}")

extractCtFiles(input_dir, output_dir)