import numpy as np
import matplotlib.pyplot as plt

timefile = open("D:/Masterarbeit_programmieren/Data/execution_time.log", "r")
file = timefile.readlines()

processedFiles = []
usedSeconds = []

for line in file:
    if line.startswith("Processed"): 
        newLines = line.split()
        processedFiles.append(newLines[1])
        usedSeconds.append(float(newLines[4]))

newListUsedSeconds = []

for i in range(len(usedSeconds) - 1):
    j = i + 1
    newListUsedSeconds.append(usedSeconds[j] - usedSeconds[i])

print(newListUsedSeconds)

print(np.mean(newListUsedSeconds))