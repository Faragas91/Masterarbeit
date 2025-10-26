import os
import shutil
import pandas as pd

# Function to parse the RNAz file
def parse_petfold_file(file_path):
    
    # Read every line in the .txt file
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith("Score"):
                score = line.split()[-1]
    return {"Score": score}

# All data
def createExcelData(data, count, nameOfFile, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith(nameOfFile):
            count += 1
            print(f"Process file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parse_petfold_file(file_path)
            file_data["File"] = file_name  
            data.append(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
    shutil.move(f"/mnt/bernhard/Masterarbeit/{excelName}.xlsx", f"/mnt/bernhard/Masterarbeit/2.Versuch/Data/PETfold/PETfold_Excel/{excelName}.xlsx")
    return count 

directory = "/mnt/bernhard/Masterarbeit/2.Versuch/Data/PETfold/With_SISSI/PETfold_PREDICTION/"

count = 0
sissi_pos_data = []
count = createExcelData(sissi_pos_data, count, "pos_sample", "sissi")

count = 0
alifoldz_data = []
count = createExcelData(alifoldz_data, count, "neg_sample_ALIFOLDz", "alifoldz")

count = 0
multiperm_mono_data = []
count = createExcelData(multiperm_mono_data, count, "neg_sample_MULTIPERM_mono", "multiperm_mono")

count = 0
multiperm_di_data = []
count = createExcelData(multiperm_di_data, count, "neg_sample_MULTIPERM_di", "multiperm_di")

count = 0
sissiz_mono_data = []
count = createExcelData(sissiz_mono_data, count, "neg_sample_SISSIz_mono", "sissiz_mono")

count = 0
sissiz_di_data = []
count = createExcelData(sissiz_di_data, count, "neg_sample_SISSIz_di", "sissiz_di")