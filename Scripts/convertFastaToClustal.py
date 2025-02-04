import os
from Bio import AlignIO
from Bio import SeqIO

SAMPLES_CLUSTAL = "C:/bla/Waste/MA/Data/"
SAMPLES_FASTA = "C:/bla/Waste/MA/Data/"

def convertFastaToClustal(inputDir):
    for file in os.listdir(inputDir):
        if file.endswith(".fasta"):
            input_file_path = os.path.join(inputDir, file)
            output_file_path = os.path.join(SAMPLES_CLUSTAL, os.path.splitext(file)[0] + ".clu")
            
            try:
                with open(input_file_path, "r") as input_file:
                    records = list(SeqIO.parse(input_file, "fasta"))
                    alignment = AlignIO.MultipleSeqAlignment(records)
                    count = AlignIO.write(alignment, output_file_path, "clustalw")
                    print(f"Converted {count} records from {file} to {output_file_path}")
            except Exception as e:
                print(f"Error processing file {file}: {e}")

convertFastaToClustal(SAMPLES_FASTA)
