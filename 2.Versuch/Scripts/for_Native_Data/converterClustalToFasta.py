import os
from Bio import SeqIO

SAMPLES_CLUSTAL = "D:/Masterarbeit/2.Versuch/Data/Native_Data/SAMPLES_CLUSTAL/"
# SAMPLES_CLUSTAL = "/mnt/sdc2/home/c2210542009/Masterarbeit/NativeData/SAMPLES_CLUSTAL/"
# SAMPLES_CLUSTAL = "/home/sredl/Masterarbeit/2.Versuch/Data/SAMPLES_CLUSTAL/"
SAMPLES_FASTA = "D:/Masterarbeit/2.Versuch/Data/Native_Data/SAMPLES_FASTA/"
# SAMPLES_FASTA = "/mnt/sdc2/home/c2210542009/Masterarbeit/NativeData/SAMPLES_FASTA/"
#SAMPLES_FASTA = "/home/sredl/Masterarbeit/2.Versuch/Data/SAMPLES_FASTA/"

if not os.path.exists(SAMPLES_FASTA):
    os.makedirs(SAMPLES_FASTA)

def convertClustalToFasta(inputDir):
    for file in os.listdir(inputDir):
        if file.endswith(".clu"):
            input_file_path = os.path.join(inputDir, file)
            output_file_path = os.path.join(SAMPLES_FASTA, os.path.splitext(file)[0] + ".fasta")

            if os.path.exists(output_file_path):
                print(f"⚠️ {output_file_path} already exists. Skipping.")
                continue
            else:
                try:
                    with open(input_file_path, "r") as input_file:
                        records = SeqIO.parse(input_file, "clustal")
                        count = SeqIO.write(records, output_file_path, "fasta")

                        if count == 0:
                            print(f"⚠️ No sequences written from {file} — file may be empty.")
                        else:
                            print(f"✅ Converted {count} records from {file} to {output_file_path}")
                except Exception as e:
                    os.remove(input_file_path)
                    print(f"❌ Error processing file {file}: {e}")
                    continue

convertClustalToFasta(SAMPLES_CLUSTAL)
