import os
import shutil

SAMPLES_FASTA = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_FASTA/"
SAMPLES_UFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_UFOLD/"

if not os.path.exists(SAMPLES_UFOLD):
    os.makedirs(SAMPLES_UFOLD)

def convertFastaToUfoldStructure(inputDir):
    for file in os.listdir(inputDir):
        file_path = os.path.join(inputDir, file)
        with open(file_path) as lines:
            sequenceCount = 0
            current_sequence = []
            for line in lines:
                if line.startswith(">"):
                    if current_sequence:
                        with open(os.path.join(SAMPLES_UFOLD, f'seq{sequenceCount}_{file}'), 'w') as output_file:
                            output_file.write("".join(current_sequence).replace("T", "U"))
                        sequenceCount += 1
                        current_sequence = [] 
                    current_sequence.append(line.strip() + '\n')
                else:
                    current_sequence.append(line.strip())
            if current_sequence:
                with open(os.path.join(SAMPLES_UFOLD, f'seq{sequenceCount}_{file}'), 'w') as output_file:
                    output_file.write(''.join(current_sequence))

convertFastaToUfoldStructure(SAMPLES_FASTA)


                            
