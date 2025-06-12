import os
import time
import subprocess
from tqdm import tqdm

SAMPLES_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_REDFOLD"
REDFOLD_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/REDFOLD_PREDICTION"

os.makedirs(REDFOLD_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def run_redfold():
    for folder_name in tqdm(['ALIFOLDz', 'MULTIPERM_MONO', 'MULTIPERM_DI', 'SISSIz_MONO', 'SISSIz_DI', 'POS_SAMPLES'], desc="REDfold"):
        sample_path = os.path.join(SAMPLES_REDFOLD, folder_name)
        log_path = os.path.join(REDFOLD_PRE_OUTPUT, f"{folder_name}.txt")
        
        with open(log_path, 'w') as log_file:
            subprocess.run(['redfold', sample_path], stdout=log_file, stderr=subprocess.STDOUT)

run_redfold()

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
