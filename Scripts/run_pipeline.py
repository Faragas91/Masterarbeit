import os
import subprocess
from concurrent.futures import ProcessPoolExecutor, as_completed
from threading import Lock

# Define variables
NEIGHBOURHOOD = "neighbourhoods/bsubtilis401.nei"
TREE = "trees/alina.tree"
ITER_POS = 100
ITER_NEG = 1000
FREQUENCIES_SINGLE = "0.422360 0.105590 0.236025 0.236025"
FREQUENCIES_DOUBLE = "0.000423 0.004228 0.012685 0.169133 0.004228 0.000423 0.262156 0.000423 0.012685 0.262156 0.000423 0.042283 0.169133 0.000423 0.042283 0.016915"
SISSI = "/home/slais/Masterarbeit/tools/sissi/sissi099"
SISSIz = "/home/slais/Masterarbeit/tools/sissiz_v3/src/SISSIz"
RNAz = "/home/slais/Masterarbeit/tools/RNAz-2.1.1/rnaz/RNAz"
ALIFOLDZ = "/home/slais/Masterarbeit/tools/shuffle-aln.pl"
MULTIPERM = "/home/slais/Masterarbeit/tools/multiperm-0.9.4/multiperm"
SAMPLES = "/home/slais/Masterarbeit/SAMPLES"
SISSIz_PRE_OUTPUT = "/home/slais/Masterarbeit/SISSIz_PREDICTION"
RNAz_PRE_OUTPUT = "/home/slais/Masterarbeit/RNAz_PREDICTION"
TMPDIR = "/home/slais/Masterarbeit/tmp"
NUM_CORES = 24  # Number of CPU cores to use

# Make sure the executables have the necessary permissions
os.chmod(SISSI, 0o755)
os.chmod(SISSIz, 0o755)
os.chmod(RNAz, 0o755)
os.chmod(MULTIPERM, 0o755)

# Create the output directories if they don't exist
os.makedirs(SAMPLES, exist_ok=True)
os.makedirs(SISSIz_PRE_OUTPUT, exist_ok=True)
os.makedirs(RNAz_PRE_OUTPUT, exist_ok=True)
os.makedirs(TMPDIR, exist_ok=True)

os.environ["TMPDIR"] = TMPDIR

# Function to run a command and return the output
def run_command(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Error running command: {command}\n{stderr.decode()}")
    return stdout.decode()

def process_file_rnaz(file):
    global current_file
    basename = os.path.splitext(file)[0]
    output_file = os.path.join(RNAz_PRE_OUTPUT, f"{basename}.txt")
    
    # Check if output file already exists
    if os.path.isfile(output_file):
        print(f"{output_file} already exists, skipping...")
        return
    
    # Run RNAz prediction
    run_command(f"{RNAz} -n {os.path.join(SAMPLES, file)} >> {output_file}")
    print(f"{output_file} finished")

def process_file_sissiz(file):
   global current_file
   basename = os.path.splitext(file)[0]
   output_file = os.path.join(SISSIz_PRE_OUTPUT, f"{basename}.txt")
    
   # Check if output file already exists
   if os.path.isfile(output_file):
       print(f"{output_file} already exists, skipping...")
       return
    
   # Run SISSIz prediction
   run_command(f"{SISSIz} --sci {os.path.join(SAMPLES, file)} >> {output_file}")
   print(f"{output_file} finished")


# Run RNAz predictions for all samples in parallel
with ProcessPoolExecutor(max_workers=NUM_CORES) as executor:
    futures = [executor.submit(process_file_rnaz, file) for file in os.listdir(SAMPLES) if file.endswith(".clu")]
    for future in as_completed(futures):
        future.result()

# Run SISSIz predictions for all samples in parallel
with ProcessPoolExecutor(max_workers=NUM_CORES) as executor:
   futures = [executor.submit(process_file_sissiz, file) for file in os.listdir(SAMPLES) if file.endswith(".clu")]
   for future in as_completed(futures):
       future.result()

print("\nProcessing completed.")
