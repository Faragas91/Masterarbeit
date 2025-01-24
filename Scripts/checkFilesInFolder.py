import os
import time

folderPath = "home/slais/Masterarbeit/RNAz_PREDICTION"

def countFiles(folder):
    return len([name for name in os.listdir(folder) if os.path.isfile(os.path.join(folder, name))])

try:
    print("Start monitoring")
    previusCounter = 0
    checkCounter = 1000
    
    start_time = time.time()
    start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
    print(f"Script started at: {start_time_str}") 

    while True:

        currentCounter = countFiles(folderPath)

        if currentCounter == checkCounter:
            checkCounter += 1000
            end_time = time.time()
            end_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
            print(f"10 files are predicted: {end_time_str}") 
            execution_time = end_time - start_time
            print(f"Differenz: {execution_time}")
            start_time = time.time()
            start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
            print(f"New start time: {start_time_str}") 

        if currentCounter != previusCounter:
            print(f"Monitoring the Files: {currentCounter} (before {previusCounter})")

            previusCounter = currentCounter

except KeyboardInterrupt:
    print("Monitoring stopped")