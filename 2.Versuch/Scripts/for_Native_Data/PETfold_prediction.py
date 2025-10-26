import os
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed
import time
import threading

# Define variables
PETfold = "/home/sredl/Masterarbeit/tools/PETfold/bin/PETfold"
SAMPLES_FASTA = "/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_FASTA"
PETfold_PRE_OUTPUT = "/home/sredl/Masterarbeit/2.Versuch/Native_Data/PETfold_PREDICTION"
NUM_CORES = 64  # Number of CPU cores to use

# Create the output directories if they don't exist
os.makedirs(PETfold_PRE_OUTPUT, exist_ok=True)

# Function to run a command and return the output
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}\n{stderr}")
    return stdout

def process_file_PETfold(file):
    basename = os.path.splitext(file)[0]
    output_file = os.path.join(PETfold_PRE_OUTPUT, f"{basename}.txt")
        
    # Check if output file already exists
    if os.path.isfile(output_file):
        print(f"{output_file} already exists, skipping...")
    else:
        # Run PETfold prediction
        run_command(f"{PETfold} -f {os.path.join(SAMPLES_FASTA, file)} >> {output_file}")
        print(f"{output_file} finished")

def increment_count():
    global count, start_time
    with lock:
        count += 1
        if count % 1000 == 0:
            elapsed_time = time.time() - start_time
            print(f"Processed {count} files in {elapsed_time:.2f} seconds")
            with open("PETfold_execution_time.log", "a") as log_file:
                log_file.write(f"Processed {count} files in {elapsed_time:.2f} seconds\n")

# Start time measurement
start_time = time.time()
start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
print(f"Script started at: {start_time_str}")

count = 0
lock = threading.Lock()

with ProcessPoolExecutor(max_workers=NUM_CORES) as executor:
    futures = {executor.submit(process_file_PETfold, file): file for file in os.listdir(SAMPLES_FASTA) if file.endswith(".fasta")}
    for future in as_completed(futures):
        future.result()
        increment_count()

print("\nProcessing completed.")

# End time measurement
end_time = time.time()
end_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
execution_time = end_time - start_time

print(f"\nScript finished at: {end_time_str}")
print(f"Total execution time: {execution_time:.2f} seconds")

# Save final execution time to file
with open("PETfold_execution_time.log", "a") as log_file:
    log_file.write(f"\nScript finished at: {end_time_str}\n")
    log_file.write(f"Total execution time: {execution_time:.2f} seconds\n")
