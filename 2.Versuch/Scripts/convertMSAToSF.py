import os
from os import path

SAMPLES_FASTA = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_FASTA/"
SAMPLES_REDFOLD = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_REDFOLD/"

# SAMPLES_FASTA = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_FASTA/"
# SAMPLES_REDFOLD = "D:/Masterarbeit/2.Versuch/Data/SAMPLES_REDFOLD/"

METHODE = {
    "ALIFOLDz": "ALIFOLDz",
    "MULTIPERM_MONO": "MULTIPERM_MONO",
    "MULTIPERM_DI": "MULTIPERM_DI",
    "SISSIz_MONO": "SISSIz_MONO",
    "SISSIz_DI": "SISSIz_DI",
    "POS": "POS_SAMPLES"
}

# Funktion zur Methode
def getMethodSubfolder(file_name):
    parts = file_name.split('_')
    if parts[2] == "ALIFOLDz":
        return METHODE["ALIFOLDz"]
    elif parts[2] == "MULTIPERM":
        if parts[3] == "mono":
            return METHODE["MULTIPERM_MONO"]
        elif parts[3] == "di":
            return METHODE["MULTIPERM_DI"]
    elif parts[2] == "SISSIz":
        if parts[3] == "mono":
            return METHODE["SISSIz_MONO"]
        elif parts[3] == "di":
            return METHODE["SISSIz_DI"]
    else:
        return METHODE["POS"]

def getSizeSubfolder(file_name):
    try:
        num_part = file_name.split("_output_")[-1].split(".")[0]
        num = int(num_part)
        if num < 5000:
            return "5000"
        elif num >= 5000 and num < 10000:
            return "10000"
        elif num >= 10000 and num < 15000:
            return "15000"
        elif num >= 15000 and num < 20000:
            return "20000"
        elif num >= 20000 and num < 25000:
            return "25000"
        elif num >= 25000 and num < 30000:
            return "30000"
        elif num >= 30000 and num < 35000:
            return "35000"
        elif num >= 35000 and num < 40000:
            return "40000"
        elif num >= 40000 and num < 45000:
            return "45000"
        elif num >= 45000 and num < 50000:
            return "50000"
        elif num >= 50000 and num < 55000:
            return "55000"
        elif num >= 55000 and num < 60000:
            return "60000"
        elif num >= 60000 and num < 65000:
            return "65000"
        elif num >= 65000 and num < 70000:
            return "70000"
        elif num >= 70000 and num < 75000:
            return "75000"
        elif num >= 75000 and num < 80000:
            return "80000"
        elif num >= 80000 and num < 85000:
            return "85000"
        elif num >= 85000 and num < 90000:
            return "90000"
        elif num >= 90000 and num < 95000:
            return "95000"
        elif num >= 95000 and num <= 100000:
            return "100000"
    except:
        return "unbekannt"

# Hauptfunktion
def convertFastaToUfoldStructure(inputDir):
    for file in os.listdir(inputDir):
        file_path = os.path.join(inputDir, file)

        method_subdir = getMethodSubfolder(file)
        size_subdir = getSizeSubfolder(file)

        out_dir = os.path.join(SAMPLES_REDFOLD, method_subdir, size_subdir)
        os.makedirs(out_dir, exist_ok=True)

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
