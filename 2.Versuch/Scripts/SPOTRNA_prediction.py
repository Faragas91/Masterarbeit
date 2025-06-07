from concurrent.futures import ProcessPoolExecutor, as_completed
import os
import subprocess
import time

SAMPLES = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_FASTA"
SPOTRNA_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SPOTRNA_PREDICTION"
NUM_PROCESSES = 5 

os.makedirs(SPOTRNA_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def run_spotrna(file):
    fileName = os.path.splitext(file)[0]
    print(f"⚙️ Processing: {file}")
    input_path = os.path.join(SAMPLES, file)
    output_path = os.path.join(SPOTRNA_PRE_OUTPUT, fileName)
    os.makedirs(output_path, exist_ok=True)

    if len(os.listdir(output_path)) == 0:
        cmd = f"python3 /mnt/sdc2/home/c2210542009/Masterarbeit/SPOT-RNA/SPOT-RNA.py --inputs {input_path} --outputs {output_path} --gpu 0"
        print(f"⚙️ Running: {cmd}") 
        result = subprocess.run(cmd, shell=True)
    else:
        print(f"✅ Was already predicted: {file}")
        return

    if result.returncode == 0:
        print(f"✅ Successfully predicted: {file}")
    else:
        print(f"❌ Error processing: {file}")

with ProcessPoolExecutor(max_workers=NUM_PROCESSES) as executor:
    futures = [executor.submit(run_spotrna, file) for file in sorted(os.listdir(SAMPLES)) if file.endswith(".fasta")]
    for future in as_completed(futures):
        pass

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
