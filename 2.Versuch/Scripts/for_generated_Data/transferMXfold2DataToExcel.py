import os
import shutil
import pandas as pd
import statistics

# Function to parse the RNAz file
def parse_mxfold2_file(file_path):
    number = []
    with open(file_path, 'r') as file:
        for line in file:
            line_row = line.strip().split()
            if len(line_row) > 1:
                value = float(line_row[1].replace("(", "").replace(")", ""))
                number.append(value)
        print(number)
        result_number = statistics.median(number)
        return result_number

# All data
def createExcelData(data, count, nameOfFile, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith(nameOfFile):
            count += 1
            print(f"Process file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parse_mxfold2_file(file_path)  
            data.append({"Score": file_data, "File": file_name})

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
    shutil.move(f"/mnt/sdc2/home/c2210542009/Masterarbeit/Scripts/{excelName}.xlsx", f"/mnt/sdc2/home/c2210542009/Masterarbeit/Data/MXfold2_Excel/{excelName}.xlsx") #f"C:/bla/Waste/MA/{excelName}.xlsx", f"C:/bla/Waste/MA/2.Versuch/Data/MXfold2_Excel/{excelName}.xlsx")
    return count

directory = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/MXfold2_PREDICTION"
#directory = "C:/bla/Waste/MA/2.Versuch/Data/MXfold2_SAMPLES"

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