import os
from os import path
import shutil

# SAMPLES_FASTA = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_FASTA/"
# SAMPLES_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/TEST_SAMPLES/SAMPLES_REDFOLD/"
SAMPLES_REDFOLD = "C:/bla/Waste/MA/2.Versuch/Data/SAMPLES_REDFOLD/"
METHODE = ["ALIFOLDz", "MULTIPERM_MONO", "MULTIPERM_DI", "SISSIz_MONO", "SISSIz_DI", "POS_SAMPLES"]

for i in METHODE:
    if not os.path.exists(os.path.join(SAMPLES_REDFOLD, i)):
        os.makedirs(os.path.join(SAMPLES_REDFOLD, i))

# if not os.path.exists(SAMPLES_REDFOLD):
#     os.makedirs(SAMPLES_REDFOLD)

# def convertFastaToUfoldStructure(inputDir):
#     for file in os.listdir(inputDir):
#         file_path = os.path.join(inputDir, file)
#         with open(file_path) as lines:
#             sequenceCount = 0
#             current_sequence = []
#             for line in lines:
#                 if line.startswith(">"):
#                     if current_sequence:
#                         with open(os.path.join(SAMPLES_REDFOLD, f'seq{sequenceCount}_{file}'), 'w') as output_file:
#                             output_file.write("".join(current_sequence).replace("T", "U"))
#                         sequenceCount += 1
#                         current_sequence = [] 
#                     current_sequence.append(line.strip() + '/n')
#                 else:
#                     current_sequence.append(line.strip())
#             if current_sequence:
#                 with open(os.path.join(SAMPLES_REDFOLD, f'seq{sequenceCount}_{file}'), 'w') as output_file:
#                     output_file.write(''.join(current_sequence))

def splitFastaFiles(inputDir):
    for file in os.listdir(inputDir):
        if file.startswith('seq'):
            name , _ = path.splitext(file)
            parts = name.split('_')
            
            if parts[3] == "ALIFOLDz":
                shutil.move(os.path.join(SAMPLES_REDFOLD, file), os.path.join(SAMPLES_REDFOLD, METHODE[0]))
            if parts[3] == "MULTIPERM_MONO":
                shutil.move(os.path.join(SAMPLES_REDFOLD, file), os.path.join(SAMPLES_REDFOLD, METHODE[1]))
            if parts[3] == "MULTIPERM_DI":
                shutil.move(os.path.join(SAMPLES_REDFOLD, file), os.path.join(SAMPLES_REDFOLD, METHODE[2]))
            if parts[3] == "SISSIz_MONO":
                shutil.move(os.path.join(SAMPLES_REDFOLD, file), os.path.join(SAMPLES_REDFOLD, METHODE[3]))
            if parts[3] == "SISSIz_DI":
                shutil.move(os.path.join(SAMPLES_REDFOLD, file), os.path.join(SAMPLES_REDFOLD, METHODE[4]))
            else:
                shutil.move(os.path.join(SAMPLES_REDFOLD, file), os.path.join(SAMPLES_REDFOLD, METHODE[5]))

# convertFastaToUfoldStructure(SAMPLES_FASTA)
splitFastaFiles(SAMPLES_REDFOLD)


                            
