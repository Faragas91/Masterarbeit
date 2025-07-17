import sys, os
from Bio import SeqIO

input_path = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_CLUSTAL"
for j in os.listdir(input_path):
    input_file = j.split("/")[-1]
    file_name = input_file.split(".")[0]
    step = 6
    full_path = os.path.join(input_path, input_file)
    out_prefix = f"C:/bla/Waste/MA/2.Versuch/Data/ClustalW_Subfiles/{file_name}"

    records = list(SeqIO.parse(full_path, "clustal"))
    if len(records) == 0:
        sys.exit("No Sequence found")

    for i in range(0, len(records), step):
        chunk = records[i:i+step]
        idx = i//step + 1
        out = f"{out_prefix}_{idx:02d}.clu"
        with open(out, "w") as handle:
            SeqIO.write(chunk, handle, "clustal")
            print(f"Write {out} with {len(chunk)} Sequences")