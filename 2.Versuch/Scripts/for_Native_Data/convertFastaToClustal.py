from Bio import SeqIO

main_direction = "/mnt/bernhard/Masterarbeit/"

records = SeqIO.parse(f"{main_direction}RF00001.fa", "fasta")
count = SeqIO.write(records, f"{main_direction}RF00001.clustal", "clustal")
print("Converted %i records" % count)