import os

SAMPLES_FASTA="/run/media/stefanre/CA6415EC6415DC4F/Masterarbeit/2.Versuch/Native_Data/SAMPLES_FASTA/"
SAMPLES_RNAFM="/run/media/stefanre/CA6415EC6415DC4F/Masterarbeit/2.Versuch/Native_Data/SAMPLES_RNAFM/"

# SAMPLES_FASTA = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_FASTA/"
# SAMPLES_RNAFM = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_RNAFM/"

os.makedirs(SAMPLES_RNAFM, exist_ok=True)

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
        out_path = os.path.join(SAMPLES_RNAFM, filename)
        print(f"Converting {filename}")
        convertFasta(in_path, out_path)
