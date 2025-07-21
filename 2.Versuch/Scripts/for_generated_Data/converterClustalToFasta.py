import os
from Bio import SeqIO

# SAMPLES_CLUSTAL = "D:/Masterarbeit_programmieren/2.Versuch/Data/SAMPLES_CLUSTAL/"
SAMPLES_CLUSTAL = "/run/media/stefanre/CA6415EC6415DC4F/Masterarbeit/2.Versuch/Native_Data/SAMPLES_CLUSTAL/"
#SAMPLES_FASTA = "D:/Masterarbeit_programmieren/2.Versuch/Data/SAMPLES_FASTA/"
SAMPLES_FASTA = "/run/media/stefanre/CA6415EC6415DC4F/Masterarbeit/2.Versuch/Native_Data/SAMPLES_FASTA/"

if not os.path.exists(SAMPLES_FASTA):
    os.makedirs(SAMPLES_FASTA)

def convertClustalToFasta(inputDir):
    for file in os.listdir(inputDir):
        if file.endswith(".clu"):
            input_file_path = os.path.join(inputDir, file)
            output_file_path = os.path.join(SAMPLES_FASTA, os.path.splitext(file)[0] + ".fasta")
            
            try:
                with open(input_file_path, "r") as input_file:
                    records = SeqIO.parse(input_file, "clustal")
                    count = SeqIO.write(records, output_file_path, "fasta")
                    print(f"Converted {count} records from {file} to {output_file_path}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

convertClustalToFasta(SAMPLES_CLUSTAL)
