import os
import shutil
import subprocess

# samplesInputDir = "D:/Masterarbeit/2.Versuch/Result/RNA-FM/"
# outputCtFiles = "D:/Masterarbeit/2.Versuch/Result/RNA-FM_DOT_NOTATION/"

samplesInputDir = "/mnt/sdc2/home/c2210542009/Masterarbeit/NativeData/RNAFM_PRE_OUTPUT/"
outputCtFiles = "/mnt/sdc2/home/c2210542009/Masterarbeit/NativeData/RNA-FM_DOT_NOTATION/"

if not os.path.exists(outputCtFiles):
    os.makedirs(outputCtFiles)

def extractCtFiles(samplesInputDir, outputCtFiles):
    for files in os.listdir(samplesInputDir):
        ctFolder = os.path.join(outputCtFiles, files)
        if not os.path.exists(ctFolder):
            os.makedirs(ctFolder)
        folders = os.path.join(samplesInputDir, files)
        for folder in os.listdir(folders):
            if folder == "pred_ct":
                predCt = os.path.join(folders, folder)
                for ct in os.listdir(predCt):
                    if ct.endswith(".ct"):
                        ctFilePath = os.path.join(predCt, ct)
                        dotFilePath = os.path.join(ctFolder, ct.replace('.ct', '.txt'))
                        evalFilePath = os.path.join(ctFolder, ct.replace('.ct', '.rnaeval.txt'))

                        cmd = f"ct2db {ctFilePath} > {dotFilePath}"
                        subprocess.run(cmd, shell=True)

                        cmd = f"RNAeval < {dotFilePath} > {evalFilePath}"
                        subprocess.run(cmd, shell=True)

                        print(f"Converted {ct} to dot notation and evaluated free energy.")
                            
extractCtFiles(samplesInputDir, outputCtFiles)
