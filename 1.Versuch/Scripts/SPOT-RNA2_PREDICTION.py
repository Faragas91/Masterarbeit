import os
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed

# Define variables
SAMPLES_FASTA = "/mnt/d/Masterarbeit/Scripts/testSamples/fasta"
SPOT_RNA2 = "/mnt/d/Masterarbeit/tools/SPOT-RNA2/run_spotrna2.sh"
SPOT_RNA2_OUTPUT = "/mnt/d/Masterarbeit/SPOT_RNA2_PREDICTION"
NUM_CORES = 2  # Number of CPU cores to use

# Make sure the executables have the necessary permissions
os.chmod(SPOT_RNA2, 0o755)

# Create the output directories if they don't exist
os.makedirs(SAMPLES_FASTA, exist_ok=True)

# Function to run a command and return the output
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}\n{stderr.decode()}")
    return stdout.decode()

def process_file_spot_rnaz2(file):
    basename = os.path.splitext(file)[0]
    output_file = os.path.join(SPOT_RNA2_OUTPUT, f"{basename}.txt")
    
    # Check if output file already exists
    if os.path.isfile(output_file):
       print(f"{output_file} already exists, skipping...")
       return
    
    # Run RNAz prediction
    run_command(f"{SPOT_RNA2} -n {os.path.join(SAMPLES_FASTA, file)} >> {output_file}")
    print(f"{output_file} finished")

# Run RNAz predictions for all samples in parallel
with ProcessPoolExecutor(max_workers=NUM_CORES) as executor:
   futures = [executor.submit(process_file_spot_rnaz2, file) for file in os.listdir(SAMPLES_FASTA) if file.endswith(".fasta")]
   for future in as_completed(futures):
       future.result()

print("\nProcessing completed.")
