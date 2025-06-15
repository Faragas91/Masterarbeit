from pathlib import Path
import os
import subprocess
from tqdm import tqdm

# Pfade
SAMPLES_REDFOLD = Path("/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/REDFOLD_PREDICTION/")
REDFOLD_RESULTS = Path("/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/REDFOLD_RESULTS/")
RNAEVAL_RESULTS = Path("/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/RNAeval_RESULTS/")
METHODE = ["ALIFOLDz", "MULTIPERM_MONO", "MULTIPERM_DI", "SISSIz_MONO", "SISSIz_DI", "POS_SAMPLES"]

REDFOLD_RESULTS.mkdir(parents=True, exist_ok=True)

def prepareForRnaeval():
    for method in METHODE:
        clean_file = SAMPLES_REDFOLD / f"{method}_clean.txt"
        if not clean_file.exists():
            print(f"⚠️ Datei nicht gefunden: {clean_file}")
            continue

        with clean_file.open("r") as f:
            lines = [line.strip() for line in f if line.strip()]

        method_out_dir = REDFOLD_RESULTS / method
        method_out_dir.mkdir(parents=True, exist_ok=True)

        for i in range(0, len(lines), 3):
            header = lines[i]
            sequence = lines[i + 1] if i + 1 < len(lines) else ""
            structure = lines[i + 2] if i + 2 < len(lines) else ""

            filename = f"{header[1:]}.fasta"
            out_path = method_out_dir / filename
            out_path.parent.mkdir(parents=True, exist_ok=True)

            with out_path.open("w") as out_file:
                out_file.write(f"{header}\n{sequence}\n{structure}\n")

        print(f"✅ Dateien für Methode {method} gespeichert in: {method_out_dir}")

def executeRnaeval(input_dir, output_dir):
    for method in METHODE:
        input_method_dir = input_dir / method
        output_method_dir = output_dir / method

        input_method_dir.mkdir(parents=True, exist_ok=True)
        output_method_dir.mkdir(parents=True, exist_ok=True)

        fasta_files = list(input_method_dir.glob("*.fasta"))
        for fasta_file in tqdm(fasta_files, desc=f"RNAeval - {method}"):
            output_file = output_method_dir / f"{fasta_file.stem}.txt"
            try:
                subprocess.run(f"RNAeval < {fasta_file} > {output_file}", shell=True, check=True)
            except subprocess.CalledProcessError as e:
                print(f"❌ Fehler bei RNAeval für {fasta_file.name}: {e}")
            else:
                print(f"✅ RNAeval für {fasta_file.name} → {output_file.name}")

prepareForRnaeval()
executeRnaeval(REDFOLD_RESULTS, RNAEVAL_RESULTS)
