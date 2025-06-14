import os
from os import path

SAMPLES_FASTA = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_FASTA/"
SAMPLES_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_REDFOLD/"
METHODE = {
    "ALIFOLDz": "ALIFOLDz",
    "MULTIPERM_MONO": "MULTIPERM_MONO",
    "MULTIPERM_DI": "MULTIPERM_DI",
    "SISSIz_MONO": "SISSIz_MONO",
    "SISSIz_DI": "SISSIz_DI",
    "POS": "POS_SAMPLES"
}

# Sicherstellen, dass alle Zielverzeichnisse existieren
for dir_name in METHODE.values():
    os.makedirs(os.path.join(SAMPLES_REDFOLD, dir_name), exist_ok=True)

def getMethodSubfolder(file_name):
    parts = file_name.split('_')
    if "ALIFOLDz" in parts:
        return METHODE["ALIFOLDz"]
    elif "MULTIPERM" in parts:
        if "mono" in parts or "MONO" in parts:
            return METHODE["MULTIPERM_MONO"]
        elif "di" in parts or "DI" in parts:
            return METHODE["MULTIPERM_DI"]
    elif "SISSIz" in parts:
        if "mono" in parts or "MONO" in parts:
            return METHODE["SISSIz_MONO"]
        elif "di" in parts or "DI" in parts:
            return METHODE["SISSIz_DI"]
    else:
        return METHODE["POS"]

def convertFastaToUfoldStructure(inputDir):
    for file in os.listdir(inputDir):
        file_path = os.path.join(inputDir, file)
        method_subdir = getMethodSubfolder(file)
        out_dir = os.path.join(SAMPLES_REDFOLD, method_subdir)

        with open(file_path) as lines:
            sequenceCount = 0
            current_header = ""
            current_sequence = []
            for line in lines:
                if line.startswith(">"):
                    if current_sequence:
                        out_file = os.path.join(out_dir, f'seq{sequenceCount}_{file}')
                        with open(out_file, 'w') as output_file:
                            output_file.write(current_header + '\n')
                            output_file.write("".join(current_sequence).replace("T", "U") + '\n')
                        sequenceCount += 1
                        current_sequence = []
                    current_header = line.strip()
                else:
                    current_sequence.append(line.strip())
            if current_sequence:
                out_file = os.path.join(out_dir, f'seq{sequenceCount}_{file}')
                with open(out_file, 'w') as output_file:
                    output_file.write(current_header + '\n')
                    output_file.write("".join(current_sequence).replace("T", "U") + '\n')

# Start der Verarbeitung
convertFastaToUfoldStructure(SAMPLES_FASTA)
