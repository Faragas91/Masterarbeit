import os
import time
import subprocess
from tqdm import tqdm

SAMPLES_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_REDFOLD"
REDFOLD_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/REDFOLD_PREDICTION"
CLEAN_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/REDFOLD_PREDICTION/"

def run_redfold():
    for folder_name in tqdm(['ALIFOLDz', 'MULTIPERM_MONO', 'MULTIPERM_DI', 'SISSIz_MONO', 'SISSIz_DI', 'POS_SAMPLES'], desc="REDfold"):
        sample_path = os.path.join(SAMPLES_REDFOLD, folder_name)
        log_path = os.path.join(REDFOLD_PRE_OUTPUT, f"{folder_name}.txt")
        
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

def extractRedFoldOutput():
    for folder_name in tqdm(['ALIFOLDz', 'MULTIPERM_MONO', 'MULTIPERM_DI', 'SISSIz_MONO', 'SISSIz_DI', 'POS_SAMPLES'], desc="Cleaning REDfold Output"):
        input_path = os.path.join(REDFOLD_PRE_OUTPUT, f"{folder_name}.txt")
        output_path = os.path.join(CLEAN_REDFOLD, f"{folder_name}_clean.txt")
        
        if not os.path.exists(CLEAN_REDFOLD):
            os.makedirs(CLEAN_REDFOLD)
        
        cleanRedfoldOutput(input_path, output_path)

os.makedirs(REDFOLD_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

run_redfold()

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")

extractRedFoldOutput()








