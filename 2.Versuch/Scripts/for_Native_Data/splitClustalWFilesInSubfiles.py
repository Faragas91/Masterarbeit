import sys, os
from Bio import SeqIO

input_file = sys.argv[1]
step = int(sys.argv[2])
out_prefix = sys.argv[3]

records = list(SeqIO.parse(input_file, "clustal"))
if len(records) == 0:
    sys.exit("No Sequence found")

for i in range(0, len(records), step):
    chunk = records[i:i+step]
    idx = i//step + 1
    out = f"{out_prefix}_{idx:02d}.clu"
    with open(out, "w") as handle:
        SeqIO.write(chunk, handle, "clustal")
        print(f"Write {out} with {len(chunk)} Sequences")