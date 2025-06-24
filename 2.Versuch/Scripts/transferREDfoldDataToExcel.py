import os
import shutil
import pandas as pd
import statistics

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