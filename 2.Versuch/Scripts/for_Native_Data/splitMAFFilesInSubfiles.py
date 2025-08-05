import sys, os
from Bio import SeqIO

# input_path = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_MAF"
input_path = "C:/bla/Waste/MA/2.Versuch/Native_Data/"
for j in os.listdir(input_path):
    input_file = j.split("/")[-1]
    splitted_file_name = input_file.split(".")[:-1]
    file_name=".".join(splitted_file_name )
    step = 6
    full_path = os.path.join(input_path, input_file)
    out_prefix = f"C:/bla/Waste/MA/2.Versuch/Native_Data/MAF_Subfiles/{file_name}"

    records = list(SeqIO.parse(full_path, "maf"))
    if len(records) == 0:
        sys.exit("No Sequence found")

    for i in range(0, len(records), step):
        chunk = records[i:i+step]
        idx = i//step + 1
        out = f"{out_prefix}_{idx:02d}.maf"
        with open(out, "w") as handle:
            SeqIO.write(chunk, handle, "maf")
            print(f"Write {out} with {len(chunk)} Sequences")