import os
from Bio import AlignIO

# INPUT: Verzeichnis mit Stockholm-Dateien
SAMPLES_STOCKHOLM = "/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_STOCKHOLM/"

# OUTPUT: Verzeichnis für Clustal-Dateien
SAMPLES_CLUSTAL = "/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_CLUSTAL/"

if not os.path.exists(SAMPLES_CLUSTAL):
    os.makedirs(SAMPLES_CLUSTAL)

def convert_stockholm_to_clustal(input_dir, output_dir):
    for file in os.listdir(input_dir):
        if file.endswith(".sto"):
            input_path = os.path.join(input_dir, file)
            output_filename = os.path.splitext(file)[0] + ".clu"
            output_path = os.path.join(output_dir, output_filename)

            try:
                alignment = AlignIO.read(input_path, "stockholm")
                AlignIO.write(alignment, output_path, "clustal")
                print(f"Converted {file} → {output_filename}")
            except Exception as e:
                print(f"❌ Fehler bei {file}: {e}")

convert_stockholm_to_clustal(SAMPLES_STOCKHOLM, SAMPLES_CLUSTAL)
