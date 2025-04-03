import os
from Bio import SeqIO

SAMPLES_CLUSTAL = "/mnt/d/Masterarbeit/Scripts/testSamples/clu"
SAMPLES_FASTA = "/mnt/d/Masterarbeit/Scripts/testSamples/fasta"

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
