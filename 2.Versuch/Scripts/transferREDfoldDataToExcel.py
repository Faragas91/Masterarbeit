import os
import shutil
import pandas as pd
import statistics

# Function to parse the RNAz file
# def parse_redfold_file(file_path):
#     number = []
#     with open(file_path, 'r') as file:
#         for line in file:
#             line_row = line.strip().split()
#             if len(line_row) > 1:
#                 value = float(line_row[1].replace("(", "").replace(")", ""))
#                 number.append(value)
#         print(number)
#         result_number = statistics.median(number)
#         return result_number

# All data
# def createExcelData(data, count, nameOfFile, excelName):
#     for file_name in os.listdir(directory):
#         if file_name.startswith(nameOfFile):
#             count += 1
#             print(f"Process file {count}: {file_name}")
#             file_path = os.path.join(directory, file_name)
#             file_data = parse_redfold_file(file_path)  
#             data.append({"Score": file_data, "File": file_name})

#     df = pd.DataFrame(data)
#     df.to_excel(f"{excelName}.xlsx", index=False)

#     print(f"Your data was succsessfully transfered to {excelName}.xlsx.")
#     shutil.move(f"/mnt/sdc2/home/c2210542009/Masterarbeit/Scripts/{excelName}.xlsx", f"/mnt/sdc2/home/c2210542009/Masterarbeit/Data/MXfold2_Excel/{excelName}.xlsx") #f"C:/bla/Waste/MA/{excelName}.xlsx", f"C:/bla/Waste/MA/2.Versuch/Data/MXfold2_Excel/{excelName}.xlsx")
#     return count

method = ["ALIFOLDz", "MULTIPERM_MONO", "MULTIPERM_DI", "SISSIz_MONO", "SISSIz_DI", "POS_SAMPLES"]
directory = f"D:/Masterarbeit/2.Versuch/Data/RNAeval_REDfold/"


def createExcelData():

    for method_name in method:
        sample_directory = os.path.join(directory, method_name)
        data = []

        for filename in os.listdir(sample_directory):
            file_path = os.path.join(sample_directory, filename)

            with open(file_path, 'r') as file:
                lines = file.readlines() 
                third_line = lines[2].strip()  
                line_row = third_line.split()
                if len(line_row) > 1:
                    print(line_row)
                    print(line_row[-1].replace("(", "").replace(")", ""))
                    value = float(line_row[-1].replace("(", "").replace(")", ""))
                    data.append({"Score": value, "File": filename})

        df = pd.DataFrame(data)
        df.to_excel(f"{method_name}.xlsx", index=False)

        print(f"Your data was succsessfully transfered to {method_name}.xlsx.")
        shutil.move(f"D:/Masterarbeit/{method_name}.xlsx", f"D:/Masterarbeit/2.Versuch/Data/RNAeval_REDfold/{method_name}.xlsx")
    
createExcelData()