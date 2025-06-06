import os
import shutil

SAMPLES_FASTA = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_FASTA/"
SAMPLES_UFOLD = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_UFOLD/"
INPUT_FILE = "C:/bla/Waste/MA/2.Versuch/Data/input.txt"

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
                            output_file.write(''.join(current_sequence))
                        sequenceCount += 1
                        current_sequence = [] 
                    current_sequence.append(line.strip() + '\n')
                else:
                    current_sequence.append(line.strip())
            if current_sequence:
                with open(os.path.join(SAMPLES_UFOLD, f'seq{sequenceCount}_{file}'), 'w') as output_file:
                    output_file.write(''.join(current_sequence))

convertFastaToUfoldStructure(SAMPLES_FASTA)
