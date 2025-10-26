import os

SAMPLES_FASTA="/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_FASTA/"
SAMPLES_BPFOLD="/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_BPFOLD/"

# SAMPLES_FASTA = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_FASTA/"
# SAMPLES_BPFOLD = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_BPFOLD/"

os.makedirs(SAMPLES_BPFOLD, exist_ok=True)

def convertFasta(infile_path, outfile_path):
    with open(infile_path, 'r') as infile, open(outfile_path, 'w') as outfile:
        seq = ""
        for line in infile:
            line = line.strip()
            if line.startswith(">"):
                if seq:
                    outfile.write(seq.replace('T', 'U').replace('t', 'u') + "\n")
                    seq = ""
                outfile.write(line + "\n")
            else:
                seq += line
        if seq:
            outfile.write(seq.replace('T', 'U').replace('t', 'u') + "\n")

for filename in os.listdir(SAMPLES_FASTA):
    if filename.endswith(".fasta"):
        in_path = os.path.join(SAMPLES_FASTA, filename)
        out_path = os.path.join(SAMPLES_BPFOLD, filename)
        print(f"Converting {filename}")
        convertFasta(in_path, out_path)
