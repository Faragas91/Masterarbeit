import subprocess
from multiprocessing import Pool
import os
import time

SAMPLES = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_FASTA"
REDFOLD_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/REDFOLD_PREDICTION"

os.makedirs(REDFOLD_PRE_OUTPUT, exist_ok=True)
samples = ['/TEST_SAMPLES1', '/TEST_SAMPLES2', '/TEST_SAMPLES3', '/TEST_SAMPLES4']

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def run_redfold(sample):
    log_file_path = os.path.join(REDFOLD_PRE_OUTPUT, f"{os.path.basename(sample)}.log")
    with open(log_file_path, 'w') as log_file:
        subprocess.run(['redfold', sample], stdout=log_file, stderr=subprocess.STDOUT)

if __name__ == '__main__':
    with Pool(processes=len(samples)) as pool:
        pool.map(run_redfold, samples)

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
