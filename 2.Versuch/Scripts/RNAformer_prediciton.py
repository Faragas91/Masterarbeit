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

def wait_for_result(path, timeout=10):
    """Warte auf Existenz & Stabilität der Ergebnisdatei."""
    start = time.time()
    last_size = -1
    while time.time() - start < timeout:
        if os.path.exists(path):
            size = os.path.getsize(path)
            if size == last_size:
                return True  # Datei ist stabil
            last_size = size
        time.sleep(0.2)
    return False

def run_ufold():
    for file in os.listdir(SAMPLES_UFOLD):
        if file.endswith(".fasta"):
            fastaFile = os.path.join(SAMPLES_UFOLD, file)
            inputFile = os.path.join(UFOLD_INPUT, file)
            try:
                # 1. Eingabe vorbereiten
                shutil.copy(fastaFile, inputFile)
                os.rename(inputFile, os.path.join(UFOLD_INPUT, "input.txt"))
                
                # 2. UFold aufrufen
                subprocess.check_call(
                    "python3 ufold_predict.py --nc False",
                    shell=True,
                    cwd="/mnt/sdc2/home/c2210542009/Masterarbeit/UFold"
                )

                # 3. Auf stabile Ergebnisdatei warten
                result_file = os.path.join(UFPOLD_RESULTS, "input_dot_ct_file.txt")
                if wait_for_result(result_file):
                    final_name = os.path.join(UFOLD_PRE_OUTPUT, file)
                    shutil.copy(result_file, final_name)
                else:
                    print(f"[WARNUNG] Ergebnisdatei instabil oder nicht gefunden für {file}")

            except Exception as e:
                print(f"Fehler bei {file}: {e}")

run_ufold()

end_time = time.time()
print(f"Finished at {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(end_time))}")
print(f"Total time: {end_time - start_time:.2f} seconds")
