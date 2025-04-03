import os
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed

# Define variables
SAMPLES_FASTA = "/mnt/d/Masterarbeit/Scripts/testSamples/fasta"
SPOT_RNA = "/mnt/d/Masterarbeit/tools/SPOT-RNA/SPOT-RNA.py"
SPOT_RNA_OUTPUT = "/mnt/d/Masterarbeit/SPOT_RNA2_PREDICTION"
NUM_PARALLEL_PROCESSES = 10  # Number of parallel processes

# Make sure the executables have the necessary permissions
os.chmod(SPOT_RNA, 0o755)

# Create the output directories if they don't exist
os.makedirs(SPOT_RNA_OUTPUT, exist_ok=True)

# Function to process a single FASTA file using SPOT-RNA
def process_fasta_file(fasta_file):
    # Define input and output paths
    input_path = os.path.join(SAMPLES_FASTA, fasta_file)
    output_folder = os.path.join(SPOT_RNA_OUTPUT, os.path.splitext(fasta_file)[0])
    os.makedirs(output_folder, exist_ok=True)
    
    # Build the SPOT-RNA command
    command = f"python3 {SPOT_RNA} --inputs {input_path} --outputs {output_folder}"
    print(f"Running command: {command}")
    
    # Execute the command
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    # Check for errors
    if result.returncode != 0:
        print(f"Error processing {fasta_file}: {result.stderr.decode()}")
    else:
        print(f"Successfully processed {fasta_file}")
    return result.returncode

# Process files in parallel
fasta_files = [file for file in os.listdir(SAMPLES_FASTA) if file.endswith(".fasta")]
with ProcessPoolExecutor(max_workers=NUM_PARALLEL_PROCESSES) as executor:
    futures = {
        executor.submit(process_fasta_file, file): file for file in fasta_files
    }
    for future in as_completed(futures):
        file = futures[future]
        try:
            future.result()
        except Exception as e:
            print(f"Error processing file {file}: {e}")

print("All files processed.")
