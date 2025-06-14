from collections import defaultdict
from tqdm import tqdm
from pathlib import Path

CLEAN_REDFOLD = Path("D:/Masterarbeit/2.Versuch/Data/REDFold")
FASTA_OUTPUT = Path("D:/Masterarbeit/2.Versuch/Data/REDFold")

if not FASTA_OUTPUT.exists():
    FASTA_OUTPUT.mkdir(parents=True)

def convertRedfoldOutputToGroupedFasta(base_input_dir, base_output_dir):

    for folder_name in tqdm(['ALIFOLDz', 'MULTIPERM_MONO', 'MULTIPERM_DI', 'SISSIz_MONO', 'SISSIz_DI', 'POS_SAMPLES'], desc="Cleaning REDfold Output"):
        input_path = base_input_dir / f"{folder_name}.txt"
        output_dir = base_output_dir / folder_name

        # Sicherstellen, dass der Ordner existiert
        output_dir.mkdir(parents=True, exist_ok=True)

        with input_path.open("r") as file:
            lines = file.readlines()

        grouped_sequences = defaultdict(list)

        i = 0
        while i < len(lines):
            if lines[i].startswith(">"):
                header = lines[i].strip()
                sequence = lines[i + 1].strip() if i + 1 < len(lines) else ""
                structure = lines[i + 2].strip() if i + 2 < len(lines) else ""

                suffix = header.split("_output_")[-1]
                key = f"output_{suffix}"

                grouped_sequences[key].append((header, sequence, structure))

                i += 3
            else:
                i += 1

        for key, entries in grouped_sequences.items():
            out_path = output_dir / f"neg_sample_ALIFOLDz_{key}.fasta"
            print(f"Writing to {out_path}")
            with out_path.open("w") as out_file:
                for header, seq, struct in entries:
                    out_file.write(f"{header}\n{seq}\n{struct}\n")
                    out_file.write("\n") 

convertRedfoldOutputToGroupedFasta(CLEAN_REDFOLD, FASTA_OUTPUT)
