import subprocess
import os
import shutil

# Verzeichnis erstellen, falls es nicht existiert
output_dir = '/mnt/sdc2/home/c2210542009/Masterarbeit/Data/DeepFoldRNA_SAMPLES'
os.makedirs(output_dir, exist_ok=True)

samplePath = '/mnt/sdc2/home/c2210542009/Masterarbeit/Data/'
total_files = [name for name in os.listdir(samplePath) if os.path.isfile(os.path.join(samplePath, name))]
totalSize = len(total_files)
print("Total Size", totalSize)

for count, filename in enumerate(total_files):
    if os.path.isfile(os.path.join(samplePath, filename)):
        # Ursprünglichen Dateipfad
        seq_file_path = os.path.join(samplePath, filename)
        
        # Kopiere die Datei in das Zielverzeichnis und benenne sie in seq.fasta um
        temp_seq_path = os.path.join(output_dir, 'seq.fasta')
        shutil.copy(seq_file_path, temp_seq_path)

        # Eingabepfad für die Verarbeitung
        input_dir = temp_seq_path

        command = ['python3', 'runDeepFoldRNA.py', '--input_dir', input_dir]

        try:
            result = subprocess.run(command, check=True, text=True, capture_output=True)
            if result.stdout:
                print("Output:", result.stdout)
            if result.stderr:
                print("Error:", result.stderr)
        except subprocess.CalledProcessError as e:
            print("Ein Fehler ist aufgetreten:", e)

        shutil.move(temp_seq_path, os.path.join(output_dir, filename))

print("Verarbeitung abgeschlossen.")