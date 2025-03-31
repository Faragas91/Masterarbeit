import os
import subprocess
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# Define variables
NEIGHBOURHOOD = "/home/slais/Masterarbeit/neighbourhoods/bsubtilis401.nei"
TREE = "/home/slais/Masterarbeit/trees/alina.tree"
ITER_POS = 100000
ITER_NEG = 1
TOTAL_FILES = 500100  # Total number of files to be processed
FREQUENCIES_SINGLE = "0.422360 0.105590 0.236025 0.236025"
FREQUENCIES_DOUBLE = "0.000423 0.004228 0.012685 0.169133 0.004228 0.000423 0.262156 0.000423 0.012685 0.262156 0.000423 0.042283 0.169133 0.000423 0.042283 0.016915"
SISSI = "/home/slais/Masterarbeit/tools/sissi/sissi099"
SISSIz = "/home/slais/Masterarbeit/tools/sissiz_v3/src/SISSIz"
RNAz = "/home/slais/Masterarbeit/tools/RNAz-2.1.1/rnaz/RNAz"
ALIFOLDZ = "/home/slais/Masterarbeit/tools/shuffle-aln.pl"
MULTIPERM = "/home/slais/Masterarbeit/tools/multiperm-0.9.4/multiperm"
SAMPLES = "/home/slais/Masterarbeit/SAMPLES"
TMPDIR = "/home/slais/Masterarbeit/tmp"

# Make sure the executables have the necessary permissions
os.chmod(SISSI, 0o755)
os.chmod(SISSIz, 0o755)
os.chmod(RNAz, 0o755)
os.chmod(MULTIPERM, 0o755)

# Create the output directories if they don't exist
os.makedirs(SAMPLES, exist_ok=True)
os.makedirs(TMPDIR, exist_ok=True)

def run_command(command):
    """Run a command and return the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout, result.stderr

def generate_positive_sample(i):
    """Generate a positive sample using SISSI."""
    sissi_output = f"{SAMPLES}/pos_sample_output_{i}.clu"
    if not os.path.exists(sissi_output):
        command = f"{SISSI} -fs {FREQUENCIES_SINGLE} -fd {FREQUENCIES_DOUBLE} -nn {NEIGHBOURHOOD} -l401 {TREE} -oc -d > {sissi_output}"
        run_command(command)
        print(f"{sissi_output} finished")
    else:
        print(f"{sissi_output} already exists, skipping...")
    return sissi_output

def generate_negative_samples(sissi_output, i):
    """Generate negative samples using SISSIz, Multiperm, and Alifoldz."""
    for z in range(1, ITER_NEG + 1):
        # SISSIz mononucleotide sample
        sissiz_mono_output = f"{SAMPLES}/neg_sample_SISSIz_mono_output_{i}_{z}.clu"
        if not os.path.exists(sissiz_mono_output):
            command = f"{SISSIz} -s -i {sissi_output} > {sissiz_mono_output}"
            run_command(command)
            print(f"{sissiz_mono_output} finished")
        else:
            print(f"{sissiz_mono_output} already exists, skipping...")

        # Multiperm mononucleotide sample
        multiperm_mono_output = f"{SAMPLES}/neg_sample_MULTIPERM_mono_output_{i}_{z}.clu"
        if not os.path.exists(multiperm_mono_output):
            command = f"{MULTIPERM} -w --conservation=none {sissi_output} && mv perm_001_pos_sample_*.clu {multiperm_mono_output}"
            run_command(command)
            print(f"{multiperm_mono_output} finished")
        else:
            print(f"{multiperm_mono_output} already exists, skipping...")

        # Alifoldz sample
        alifoldz_output = f"{SAMPLES}/neg_sample_ALIFOLDz_output_{i}_{z}.clu"
        if not os.path.exists(alifoldz_output):
            command = f"perl {ALIFOLDZ} < {sissi_output} > {alifoldz_output}"
            run_command(command)
            print(f"{alifoldz_output} finished")
        else:
            print(f"{alifoldz_output} already exists, skipping...")

def main():
    # Generate positive samples
    with ProcessPoolExecutor(max_workers=64) as executor:
        futures = {executor.submit(generate_positive_sample, i): i for i in range(1, ITER_POS + 1)}
        for future in as_completed(futures):
            sissi_output = future.result()
            generate_negative_samples(sissi_output, futures[future])

if __name__ == "__main__":
    main()