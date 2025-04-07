import subprocess
import os
import shutil

count = 0
samplePath = 'C:/bla/Waste/MA/2.Versuch/Data/'
totalSize = len([name for name in os.listdir(samplePath) if os.path.isfile(os.path.join(samplePath, name))])
print("Total Size", totalSize)
while count < totalSize:

    for filename in os.listdir(samplePath):
        count += 1
        # if os.path.isfile(os.path.join(samplePath, filename)):
        #     os.rename(f"C:/bla/Waste/MA/2.Versuch/Data/{filename}", "C:/bla/Waste/MA/2.Versuch/Data/seq.fasta")
        #     shutil.move("C:/bla/Waste/MA/2.Versuch/Data/seq.fasta", "C:/bla/Waste/MA/2.Versuch/test/seq.fasta")

        print(count)
    # input_dir = "<path to input directory>"

    # command = ['python3', 'runDeepFoldRNA.py', '--input_dir', input_dir]

    # try:
    #     result = subprocess.run(command, check=True, text=True, capture_output=True)
    #     print("Output:", result.stdout)  # Ausgabe des Skripts
    #     print("Error:", result.stderr)    # Fehlerausgabe, falls vorhanden
    # except subprocess.CalledProcessError as e:
    #     print("Ein Fehler ist aufgetreten:", e)
