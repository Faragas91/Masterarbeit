import os
import shutil
import pandas as pd

# Function to parse the RNAz file
def parse_mxfold2_file(file_path):
    # Define the keys for the relevant columns (starting with column 4)
    with open(file_path, 'r') as file:
        first_line = file.readline().strip().split()

    return first_line


# All data
def createExcelData(data, count, nameOfFile, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith(nameOfFile):
            count += 1
            print(f"Process file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parse_mxfold2_file(file_path)
            file_data["File"] = file_name  
            data.append(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
    shutil.move(f"C:/bla/Waste/MA/{excelName}.xlsx", f"C:/bla/Waste/MA/2.Versuch/Data/MXfold2_Excel/{excelName}.xlsx")
    return count

#directory = "D:/Masterarbeit_programmieren/2.Versuch/Data/MXfold2_SAMPLES/"
directory = "C:/bla/Waste/MA/2.Versuch/Data/MXfold2_SAMPLES"

count = 0
alifoldz_data = []
count = createExcelData(alifoldz_data, count, "neg_sample_ALIFOLDz", "alifoldz")

count = 0
sissi_pos_data = []
count = createExcelData(sissi_pos_data, count, "pos_sample", "sissi")