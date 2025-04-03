import os
from Bio import AlignIO
from Bio import SeqIO

SAMPLES_STOCKHOLM = "C:/bla/Waste/MA/Data/"
SAMPLES_FASTA = "C:/bla/Waste/MA/Data/"

def convertStockholmToFasta(inputDir):
    for file in os.listdir(inputDir):
        if file.endswith(".stockholm"):
            input_file_path = os.path.join(inputDir, file)
            output_file_path = os.path.join(SAMPLES_FASTA, os.path.splitext(file)[0] + ".fasta")
            
            try:
                alignment = SeqIO.parse(input_file_path, "stockholm")
                count = SeqIO.write(alignment, output_file_path, "fasta")
                print(f"Converted {count} records from {file} to {output_file_path}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

convertStockholmToFasta(SAMPLES_STOCKHOLM)