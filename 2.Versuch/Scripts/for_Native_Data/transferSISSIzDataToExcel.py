import os
import shutil
import pandas as pd

# Function to parse the RNAz file
def parse_sissiz_file(file_path):
    # Define the keys for the relevant columns (starting with column 4)
    keys = [
        "Mean Pairwise Identity (MPI) of the input alignment",
        "Average MPI of the sampled alignments.",
        "Standard deviation of the MPIs of the sampled alignments",
        "Structural Conservation Index (SCI)",
        "GC-Content",
        "RNAalifold consensus Minimum Free Energy (MFE) of the original alignment.",
        "Average consensus MFE in the sampled alignments",
        "Standard deviation of the consensus MFE in the sampled alignments",
        "z-score calculated from 7. 8. and 9."
    ]

    with open(file_path, 'r') as file:
        first_line = file.readline().strip().split()  # Entferne Leerzeichen und teile in eine Liste

    values = first_line[4:]  
    data = {key: value for key, value in zip(keys, values)}

    return data


# All data
def createExcelData(data, count, nameOfFile, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith(nameOfFile):
            count += 1
            print(f"Process file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parse_sissiz_file(file_path)
            file_data["File"] = file_name  
            data.append(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

<<<<<<< HEAD
    output_dir = "D:/Masterarbeit/2.Versuch/Result/Native_Results/SISSIz_Excel"
=======
    output_dir = "/mnt/hdd/Masterarbeit/2.Versuch/Native_Data/SISSIz_Excel"
>>>>>>> 3e299e8a3582ae2fe36abc74c406ce7795042ba1
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
<<<<<<< HEAD
    shutil.move(f"D:/Masterarbeit/{excelName}.xlsx", f"D:/Masterarbeit/2.Versuch/Result/Native_Results/SISSIz_Excel/{excelName}.xlsx")
=======
    shutil.move(f"/mnt/hdd/Masterarbeit/{excelName}.xlsx", f"/mnt/hdd/Masterarbeit/2.Versuch/Native_Data/SISSIz_Excel/{excelName}.xlsx")
>>>>>>> 3e299e8a3582ae2fe36abc74c406ce7795042ba1
    return count

def createNativeExcelData(data, count, excelName):
    for file_name in os.listdir(directory):
        if file_name.startswith("neg_sample"):
            continue
        else:
            count += 1
            print(f"Process native file {count}: {file_name}")
            file_path = os.path.join(directory, file_name)
            file_data = parse_sissiz_file(file_path)
            file_data["File"] = file_name
            data.append(file_data)

    df = pd.DataFrame(data)
    df.to_excel(f"{excelName}.xlsx", index=False)

<<<<<<< HEAD
    output_dir = "D:/Masterarbeit/2.Versuch/Result/Native_Results/SISSIz_Excel"
=======
    output_dir = "/mnt/hdd/Masterarbeit/2.Versuch/Native_Data/SISSIz_Excel"
>>>>>>> 3e299e8a3582ae2fe36abc74c406ce7795042ba1
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
<<<<<<< HEAD
    shutil.move(f"D:/Masterarbeit/{excelName}.xlsx", f"D:/Masterarbeit/2.Versuch/Result/Native_Results/SISSIz_Excel/{excelName}.xlsx")
    return count

directory = "D:/Masterarbeit/2.Versuch/Result/Native_Results/SISSIz_PREDICTION/"
=======
    shutil.move(f"/mnt/hdd/Masterarbeit/{excelName}.xlsx", f"/mnt/hdd/Masterarbeit/2.Versuch/Native_Data/SISSIz_Excel/{excelName}.xlsx")
    return count

directory = "/mnt/hdd/Masterarbeit/2.Versuch/Native_Data//SISSIz_PREDICTION/"
>>>>>>> 3e299e8a3582ae2fe36abc74c406ce7795042ba1

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