import os
import shutil
import pandas as pd

# Function to parse the RNAz file
def parse_rnaz_file(file_path):
    data = {}
    warnings = []

    # Datei zeilenweise lesen
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()  # disable spaces
            if line.startswith("WARNING"):
                warnings.append(line)
            elif ": " in line:  # see keys and values
                key, value = line.split(": ", 1)
                data[key] = value
            if line.startswith("######################################################################"):
                break

    # Collects warnings
    data["Warnings"] = "; ".join(warnings)
    return data

# All ALIFOLD data
def createExcelData(data, count, nameOfFile, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith(nameOfFile):
            count += 1
            print(f"Verarbeite Datei {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parse_rnaz_file(file_path)
            file_data["File"] = file_name  
            file_data["Count"] = count
            data.append(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

    print(f"Daten erfolgreich extrahiert und in {excelName}.xlsx gespeichert.")
    return count 

directory = "D:/Masterarbeit/Scripts/testSamples/RNAz_Samples" 

count = 0

sissi_pos_data = []
count = createExcelData(sissi_pos_data, count, "pos_sample", "sissi")

alifoldz_data = []
count = createExcelData(alifoldz_data, count, "neg_sample_ALIFOLDz", "alifoldz")


multiperm_mono_data = []
count = createExcelData(multiperm_mono_data, count, "neg_sample_MULTIPERM_mono", "multiperm_mono")


multiperm_di_data = []
count = createExcelData(multiperm_di_data, count, "neg_sample_MULTIPERM_di", "multiperm_di")


sissiz_mono_data = []
count = createExcelData(sissiz_mono_data, count, "neg_sample_SISSIz_mono", "sissiz_mono")

sissiz_di_data = []
count = createExcelData(sissiz_di_data, count, "neg_sample_SISSIz_di", "sissiz_di")

