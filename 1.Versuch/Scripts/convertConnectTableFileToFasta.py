def ctToFasta(ct_file, fasta_file, sequence_name="B_subtilis"):
    with open(ct_file, "r") as ct, open(fasta_file, "w") as fasta:
        lines = ct.readlines()
        
        sequence = "".join(line.split()[1] for line in lines[1:])
        
        fasta.write(f">{sequence_name}\n") 
        fasta.write(sequence + "\n")

ctToFasta("D:\Masterarbeit_programmieren\Data\B.subtilis.ct2", "D:\Masterarbeit_programmieren\Data\B.subtilis.fasta")
