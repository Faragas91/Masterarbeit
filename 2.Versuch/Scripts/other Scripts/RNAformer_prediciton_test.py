from concurrent.futures import ThreadPoolExecutor, as_completed
import os
import subprocess
import time

SAMPLES_RNAFORMER = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_RNAFORMER"
RNAFORMER_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/UFOLD_PREDICTION"
NUM_THREADS = 6 

os.makedirs(RNAFORMER_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def run_rnaformer(file):
    basename = os.path.splitext(file)[0]
    input_path = os.path.join(SAMPLES_RNAFORMER, file)
    output_file = os.path.join(RNAFORMER_PRE_OUTPUT, f"{basename}.txt")

    if os.path.isfile(output_file):
        print(f"{output_file} already exists. Skipping.")
        return

    cmd = f"python infer_RNAformer.py -c 6 -s GCCCGCAUGGUGAAAUCGGUAAACACAUCGCACUAAUGCGCCGCCUCUGGCUUGCCGGUUCAAGUCCGGCUGCGGGCACCA --state_dict models/RNAformer_32M_state_dict_intra_family_finetuned.pth --config models/RNAformer_32M_config_intra_family_finetuned.yml > {output_file} 2>&1"
    process = subprocess.run(cmd, shell=True)
    
    if process.returncode != 0:
        print(f"⚠️ Error processing: {file}")
    else:
        print(f"✅ Finished: {file}")

with ThreadPoolExecutor(max_workers=NUM_THREADS) as executor:
    futures = [executor.submit(run_rnaformer, file) for file in sorted(os.listdir(SAMPLES_RNAFORMER)) if file.endswith(".fasta")]
    for future in as_completed(futures):
        pass

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
