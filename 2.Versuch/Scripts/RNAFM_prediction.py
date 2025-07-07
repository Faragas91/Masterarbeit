from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import subprocess
import time

SAMPLES_PATH = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/"
SAMPLES_FASTA = os.path.join(SAMPLES_PATH, "SAMPLES_FASTA")
RNAFM_PRE_OUTPUT = os.path.join(SAMPLES_PATH, "RNAFM_PRE_OUTPUT")
NUM_THREADS = 15

os.makedirs(RNAFM_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def runRNAFM(file):
    basename = os.path.splitext(file)[0]
    input_path = os.path.join(SAMPLES_FASTA, file)
    output_path = os.path.join(RNAFM_PRE_OUTPUT, basename)

    if os.path.exists(output_path):
        print(f"{output_path} already exists. Skipping.")
        return

    cmd = f"python launch/predict.py --config=pretrained/ss_prediction.yml --data_path={input_path} --save_dir={output_path} --save_frequency 1"
    
    process = subprocess.run(cmd, shell=True)

    if process.returncode != 0:
        print(f"⚠️ Error processing: {file}")
    else:
        print(f"✅ Finished: {file}")

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    futures = [
        executor.submit(runRNAFM, file)
        for file in sorted(os.listdir(SAMPLES_FASTA))
        if file.endswith(".fasta")
    ]
    for future in as_completed(futures):
        pass

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
