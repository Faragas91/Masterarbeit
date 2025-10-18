import os
import subprocess
import time
from concurrent.futures import ProcessPoolExecutor, as_completed

# === Parameter ===
BASE_DIR = "/mnt/sdc2/home/c2210542009/Masterarbeit"
MODEL_DIRS = [
    f"{BASE_DIR}/BPfold/model_predict_1",
    f"{BASE_DIR}/BPfold/model_predict_2",
    f"{BASE_DIR}/BPfold/model_predict_3",
    f"{BASE_DIR}/BPfold/model_predict_4",
    f"{BASE_DIR}/BPfold/model_predict_5",
    f"{BASE_DIR}/BPfold/model_predict_6",
    f"{BASE_DIR}/BPfold/model_predict_7",
    f"{BASE_DIR}/BPfold/model_predict_8",
    f"{BASE_DIR}/BPfold/model_predict_9",
    f"{BASE_DIR}/BPfold/model_predict_10",
    f"{BASE_DIR}/BPfold/model_predict_11",
    f"{BASE_DIR}/BPfold/model_predict_12",
    f"{BASE_DIR}/BPfold/model_predict_13",
    f"{BASE_DIR}/BPfold/model_predict_14",
    f"{BASE_DIR}/BPfold/model_predict_15",
    f"{BASE_DIR}/BPfold/model_predict_16",
    f"{BASE_DIR}/BPfold/model_predict_17",
    f"{BASE_DIR}/BPfold/model_predict_18",
    f"{BASE_DIR}/BPfold/model_predict_19",
    f"{BASE_DIR}/BPfold/model_predict_20",
    f"{BASE_DIR}/BPfold/model_predict_21",
    f"{BASE_DIR}/BPfold/model_predict_22",
    f"{BASE_DIR}/BPfold/model_predict_23",
    f"{BASE_DIR}/BPfold/model_predict_24",
]

SAMPLES_BPFOLD = f"{BASE_DIR}/Data/TEST_SAMPLES/SAMPLES_BPFOLD"
BPFOLD_PRE_OUTPUT = f"{BASE_DIR}/Data/BPFOLD/With_SISSI/BPFOLD_PREDICTION"

os.makedirs(BPFOLD_PRE_OUTPUT, exist_ok=True)

def run_bpfold(model_dir, fasta_file):
    basename = os.path.splitext(fasta_file)[0]
    output_file = os.path.join(BPFOLD_PRE_OUTPUT, f"{basename}.csv")

    if os.path.exists(output_file):
        print(f"✅ {basename}.csv existiert bereits, überspringe...")
        return

    cmd = (
        f"BPfold -c {model_dir} "
        f"-i {os.path.join(SAMPLES_BPFOLD, fasta_file)} "
        f"-o {BPFOLD_PRE_OUTPUT} "
        f"--out_type csv "
        f"-g 0 "
        f"--num_workers 2 "
        f"--batch_size 4 "
        f"--hide_dbn "
        f"--ignore_nc "
    )
    print(f"Start BPFold for {fasta_file} with module {model_dir}")
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    stdout, stderr = process.communicate()

    if process.returncode != 0:
        print(f"❌ Issue {fasta_file} ({model_dir}):\n{stderr}")
    else:
        print(f"✅ {basename}.csv finished ({model_dir})")

# === Laufzeitmessung ===
start_time = time.time()
start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
print(f"Script started at: {start_time_str}")

# === Alle FASTA-Dateien einsammeln ===
files = [f for f in os.listdir(SAMPLES_BPFOLD) if f.endswith(".fasta")]
files.sort()  # stabil, gleichmäßige Verteilung

# === Round-Robin-Verteilung der Modelle ===
tasks = []
for i, fasta_file in enumerate(files):
    model_dir = MODEL_DIRS[i % len(MODEL_DIRS)]  # wechselnde Modelle
    tasks.append((model_dir, fasta_file))

# === Parallele Ausführung ===
with ProcessPoolExecutor(max_workers=len(MODEL_DIRS)) as executor:
    futures = {executor.submit(run_bpfold, model_dir, fasta_file): fasta_file for model_dir, fasta_file in tasks}

    for future in as_completed(futures):
        future.result()

end_time = time.time()
print(f"\n🏁 Finished at {end_time - start_time:.2f} seconds.")
