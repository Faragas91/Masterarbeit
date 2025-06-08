import os

SAMPLES_FASTA = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_FASTA"
SAMPLES_RNAFORMER = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_RNAFORMER/"

if not os.path.exists(SAMPLES_RNAFORMER):
    os.makedirs(SAMPLES_RNAFORMER)

def convertFastaToRNAformerStructure(inputDir):
    for file in os.listdir(inputDir):
        file_path = os.path.join(inputDir, file)

        with open(file_path) as f:
            sequenceCount = -1
            current_sequence = []

            for line in f:
                line = line.strip()
                if line.startswith(">"):
                    if current_sequence:
                        output_path = os.path.join(SAMPLES_RNAFORMER, f"seq{sequenceCount}_{file}")
                        with open(output_path, 'w') as out_f:
                            out_f.write("".join(current_sequence))
                        current_sequence = []

                    sequenceCount += 1 
                else:
                    current_sequence.append(line)

            if current_sequence:
                output_path = os.path.join(SAMPLES_RNAFORMER, f"seq{sequenceCount}_{file}")
                with open(output_path, 'w') as out_f:
                    out_f.write("".join(current_sequence))

convertFastaToRNAformerStructure(SAMPLES_FASTA)
