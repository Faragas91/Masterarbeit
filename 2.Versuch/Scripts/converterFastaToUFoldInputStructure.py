import os
import shutil

SAMPLES_FASTA = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_FASTA/"
SAMPLES_UFOLD = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_UFOLD/"
INPUT_FILE = "C:/bla/Waste/MA/2.Versuch/Data/input.txt"

if not os.path.exists(SAMPLES_UFOLD):
    os.makedirs(SAMPLES_UFOLD)

def convertFastaToUfoldStructure(inputDir):
    for file in os.listdir(inputDir):
        lineBreak = False
        with open(INPUT_FILE, 'w') as input_file:
            pass
        file_path = os.path.join(inputDir, file)
        with open(file_path) as lines:
            for line in lines:
                if line.startswith(">"):
                    with open(INPUT_FILE, 'a') as input_file:
                        if lineBreak:
                           input_file.write('\n' + line.strip() + '\n') 
                        else:
                            input_file.write(line.strip() + '\n')
                if line.startswith(("A", "T", "G", "C", "U")):
                    with open(INPUT_FILE, 'a') as input_file:
                        input_file.write(line.strip())
                    lineBreak = True
        os.rename(INPUT_FILE, file)
        shutil.move(file, SAMPLES_UFOLD)

convertFastaToUfoldStructure(SAMPLES_FASTA)
