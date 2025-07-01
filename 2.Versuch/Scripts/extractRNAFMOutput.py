import os
import shutil

inputDir = "C:/bla/Waste/MA/2.Versuch/Result/RNA-FM/"
outputDir = "C:/bla/Waste/MA/2.Versuch/Result/RNA-FM_CT/"

if not os.path.exists(outputDir):
    os.makedirs(outputDir)

def extractCtFiles(inputDir, outputDir):
    for files in os.listdir(inputDir):
        ctFolder = os.path.join(outputDir, files)
        if not os.path.exists(ctFolder):
            os.makedirs(ctFolder)
        folders = os.path.join(inputDir, files)
        for folder in os.listdir(folders):
            if folder == "pred_ct":
                predCt = os.path.join(folders, folder)
                for ct in os.listdir(predCt):
                    if ct.endswith(".ct"):
                        shutil.copy(os.path.join(predCt, ct), ctFolder)

extractCtFiles(inputDir, outputDir)