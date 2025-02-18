import os
from Bio import AlignIO
from Bio import SeqIO

SAMPLES_STOCKHOLM = "/mnt/d/Masterarbeit/Scripts/Data/"
SAMPLES_FASTA = "/mnt/d/Masterarbeit/Scripts/Data/"

def convertStockholmToFasta(inputDir):
    for file in os.listdir(inputDir):
        if file.endswith(".clu"):
            input_file_path = os.path.join(inputDir, file)
            output_file_path = os.path.join(SAMPLES_FASTA, os.path.splitext(file)[0] + ".fasta")
            
            try:
                alignment = AlignIO.read(input_file_path, "stockholm")
                count = AlignIO.write(alignment, output_file_path, "stockholm")
                print(f"Converted {count} records from {file} to {output_file_path}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

convertStockholmToFasta(SAMPLES_STOCKHOLM)