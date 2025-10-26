from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import subprocess
import time

SAMPLES = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_FASTA"
MXFOLD2_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/MXfold2_PREDICTION"
NUM_THREADS = 6 

os.makedirs(MXFOLD2_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def run_mxfold2(file):
    basename = os.path.splitext(file)[0]
    input_path = os.path.join(SAMPLES, file)
    output_file = os.path.join(MXFOLD2_PRE_OUTPUT, f"{basename}.txt")

    if os.path.isfile(output_file):
        print(f"{output_file} already exists. Skipping.")
        return

    cmd = f"mxfold2 predict --param model.pth --model MixC --gpu 0 {input_path} > {output_file} 2>&1"
    process = subprocess.run(cmd, shell=True)
    
    if process.returncode != 0:
        print(f"⚠️ Error processing: {file}")
    else:
        print(f"✅ Finished: {file}")

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    futures = [executor.submit(run_mxfold2, file) for file in sorted(os.listdir(SAMPLES)) if file.endswith(".fasta")]
    for future in as_completed(futures):
        pass

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
