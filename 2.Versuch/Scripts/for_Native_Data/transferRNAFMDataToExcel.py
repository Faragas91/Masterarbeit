import os
import shutil
import pandas as pd
import statistics

def parseRnafmFile(file_path, parent_folder):
    results = []
    for fileName in os.listdir(file_path):
        if fileName.endswith(".rnaeval.txt"):
            fileRnaeval = os.path.join(file_path, fileName)
            mfe_value = None
            with open(fileRnaeval, 'r') as file:
                for line in file:
                    line_row = line.strip().split()
                    if len(line_row) > 1:
                        try:
                            mfe_value = float(line_row[-1].replace("(", "").replace(")", ""))
                            break
                        except ValueError:
                            continue
            if mfe_value is not None:
                results.append({
                    "File": fileName,
                    "ParentFolder": parent_folder,
                    "Score": mfe_value
                })
    return results

def createExcelData(data, count, nameOfFile, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith(nameOfFile):
            count += 1
            print(f"Process file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parseRnafmFile(file_path, file_name)
            data.extend(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

    output_dir = "C:/bla/Waste/MA/2.Versuch/Result/Native_Results/RNAFM_Excel"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
    # shutil.move(f"D:/Masterarbeit/{excelName}.xlsx", f"D:/Masterarbeit/2.Versuch/Result/Native_Results/RNAFM_Excel/{excelName}.xlsx") 
    # return count    
    
    shutil.move(f"C:/bla/Waste/MA/{excelName}.xlsx", f"C:/bla/Waste/MA/2.Versuch/Result/Native_Results/RNAFM_Excel/{excelName}.xlsx") 
    return count

def createNativeExcelData(data, count, excelName):
    for file_name in os.listdir(directory):
        if not file_name.startswith("neg_sample"):
            count += 1
            print(f"Process native file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parseRnafmFile(file_path, file_name)
            data.extend(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

    output_dir = "C:/bla/Waste/MA/2.Versuch/Result/Native_Results/RNAFM_Excel"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
    # shutil.move(f"D:/Masterarbeit/{excelName}.xlsx", f"D:/Masterarbeit/2.Versuch/Result/Native_Results/RNAFM_Excel/{excelName}.xlsx")
    # return count   
  
    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
    shutil.move(f"C:/bla/Waste/MA/{excelName}.xlsx", f"C:/bla/Waste/MA/2.Versuch/Result/Native_Results/RNAFM_Excel/{excelName}.xlsx")
    return count 

# directory = "D:/Masterarbeit/2.Versuch/Result/Native_Results/RNA-FM_DOT_NOTATION/"
directory = "C:/bla/Waste/MA/2.Versuch/Result/Native_Results/RNA-FM_DOT_NOTATION/"
excelDirectory = "C:/bla/Waste/MA/2.Versuch/Result/Native_Results/RNA-FM_Excel/"

if not os.path.exists(excelDirectory):
    os.makedirs(excelDirectory)

count = 0
pos_data = []
count = createNativeExcelData(pos_data, count, "native")

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