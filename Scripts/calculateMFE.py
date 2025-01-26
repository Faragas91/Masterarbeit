import os

def calculate_mfe(fasta_file):
    os.system(f"D:/Masterarbeit_old/tools\ViennaRNA-2.6.4/RNAfold < {fasta_file}")

fasta_file = "D:/Masterarbeit/Scripts/neg_sample_ALIFOLDz_output_7_890.fasta"
calculate_mfe(fasta_file)
