from Bio import AlignIO
import os

# SAMPLES_CLUSTAL = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_CLUSTAL/"
# SAMPLES_STOCKHOLM = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_STOCKHOLM/"

SAMPLES_CLUSTAL = "/home/sredl/Masterarbeit/2.Versuch/Data/SAMPLES_CLUSTAL/"
SAMPLES_STOCKHOLM = "/home/sredl/Masterarbeit/2.Versuch/Data/SAMPLES_STOCKHOLM/"

os.makedirs(SAMPLES_STOCKHOLM, exist_ok=True)

for file in os.listdir(SAMPLES_CLUSTAL):
    new_file = os.path.splitext(file)[0]
    AlignIO.convert(f"{SAMPLES_CLUSTAL}{new_file}.clu", "clustal", f"{SAMPLES_STOCKHOLM}{new_file}.sto", "stockholm")
    print(f"Converted Clustal to Stockholm: {new_file}")