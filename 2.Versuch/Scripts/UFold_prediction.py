import os
import subprocess
import time
import shutil

SAMPLES_UFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_UFOLD"
UFOLD_INPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/UFold/data"
UFPOLD_RESULTS = "/mnt/sdc2/home/c2210542009/Masterarbeit/UFold/results"
UFOLD_PRE_OUTPUT = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/UFOLD_PREDICTION"

os.makedirs(UFOLD_PRE_OUTPUT, exist_ok=True)

start_time = time.time()
print(f"Started at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(start_time))}")

def run_ufold():
    for file in os.listdir(SAMPLES_UFOLD):
        if file.endswith(".fasta"):
            fastaFile = os.path.join(SAMPLES_UFOLD, file)
            inputFile = os.path.join(UFOLD_INPUT, file)
            try:
                shutil.copy(fastaFile, inputFile)
                os.rename(inputFile, os.path.join(UFOLD_INPUT, "input.txt"))
                
                subprocess.run(
                    "python3 ufold_predict.py --nc False",
                    shell=True,
                    cwd="/mnt/sdc2/home/c2210542009/Masterarbeit/UFold"
                )
                result_file = os.path.join(UFPOLD_RESULTS, "input_dot_ct_file.txt")
                shutil.copy(result_file, UFOLD_PRE_OUTPUT)
                os.rename(os.path.join(UFOLD_PRE_OUTPUT, result_file), file)

            except Exception as e:
                print(f"Fehler bei {file}: {e}")

run_ufold()

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
