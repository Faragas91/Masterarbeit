from Bio import AlignIO
import os

# SAMPLES_CLUSTAL = "/mnt/bernhard/Masterarbeit/2.Versuch/Data/SAMPLES_CLUSTAL/"
# SAMPLES_MAF = "/mnt/bernhard/Masterarbeit/2.Versuch/Data/SAMPLES_MAF/"
SAMPLES_CLUSTAL = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_CLUSTAL/"
SAMPLES_MAF = "/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_MAF/"

if not os.path.exists(SAMPLES_MAF):
    os.makedirs(SAMPLES_MAF)

def convertClustalToMAF(inputDir, outputDir):
    for file in os.listdir(inputDir):
        if file.endswith(".clu"):
            input_file_path = os.path.join(inputDir, file)
            output_file_path = os.path.join(outputDir, os.path.splitext(file)[0] + ".maf")

            if os.path.exists(output_file_path):
                print(f"⚠️ {output_file_path} already exists. Skipping.")
                continue
            else:
                try:
                    with open(input_file_path, "r") as input_handle, open(output_file_path, "w") as output_handle:
                        alignments = AlignIO.parse(input_handle, "clustal")
                        count = AlignIO.write(alignments, output_handle, "maf")

                        if count == 0:
                            print(f"⚠️ No sequences written from {file} — file may be empty.")
                        else:
                            print(f"✅ Converted {count} alignments from {file} to {output_file_path}")
                except Exception as e:
                    os.remove(input_file_path)
                    print(f"❌ Error processing file {file}: {e}")
                    continue
            
convertClustalToMAF(SAMPLES_CLUSTAL, SAMPLES_MAF)