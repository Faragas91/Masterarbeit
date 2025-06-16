import os
import time
import subprocess
from tqdm import tqdm

SAMPLES_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_REDFOLD"
REDFOLD_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/REDFOLD_PREDICTION"
CLEAN_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/REDFOLD_PREDICTION/"

def run_redfold(subfolder):
    for folder_name in tqdm(['ALIFOLDz', 'MULTIPERM_MONO', 'MULTIPERM_DI', 'SISSIz_MONO', 'SISSIz_DI', 'POS_SAMPLES'], desc="REDfold"):
        sample_path = os.path.join(SAMPLES_REDFOLD, folder_name, subfolder)
        log_path = os.path.join(REDFOLD_PRE_OUTPUT, f"{folder_name}_{subfolder}.txt")
        
        with open(log_path, 'w') as log_file:
            subprocess.run(['redfold', sample_path], stdout=log_file, stderr=subprocess.STDOUT)

def cleanRedfoldOutput(input_path, output_path):
    with open(input_path, "r") as infile:
        lines = infile.readlines()
    
    # Find the first line that starts with '>'
    for i, line in enumerate(lines):
        if line.startswith(">"):
            break
    
    # Write the cleaned lines to the output file
    with open(output_path, "w") as outfile:
        outfile.writelines(lines[i:])

def extractRedFoldOutput(subfolder):
    for folder_name in tqdm(['ALIFOLDz', 'MULTIPERM_MONO', 'MULTIPERM_DI', 'SISSIz_MONO', 'SISSIz_DI', 'POS_SAMPLES'], desc="Cleaning REDfold Output"):
        input_path = os.path.join(REDFOLD_PRE_OUTPUT, f"{folder_name}_{subfolder}.txt")
        output_path = os.path.join(CLEAN_REDFOLD, f"{folder_name}_{subfolder}_clean.txt")
        
        if not os.path.exists(CLEAN_REDFOLD):
            os.makedirs(CLEAN_REDFOLD)
        
        cleanRedfoldOutput(input_path, output_path)

os.makedirs(REDFOLD_PRE_OUTPUT, exist_ok=True)

sample_sizes = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000]

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

for size in sample_sizes:
    run_redfold(str(size))


end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")

for size in sample_sizes:
    extractRedFoldOutput(str(size))

