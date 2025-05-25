#!/bin/bash

# Absoluter Pfad zum DeepFoldRNA-Verzeichnis
DEEPFOLD_DIR="/pfad/zu/DeepFoldRNA"

# Pfad zu allen FASTA-Dateien
INPUT_DIR="/pfad/zu/deinen/fasta_files"

# Zielverzeichnis für alle Ergebnisse
OUTPUT_ROOT="/pfad/zu/deinen/ergebnissen"

# Optional: wie viele Verfeinerungsschritte
REFINE_STEPS=5000

# Für jede FASTA-Datei im Eingabeverzeichnis
for fasta_file in "$INPUT_DIR"/*.fasta; do
    # Dateiname ohne Pfad und Endung
    filename=$(basename "$fasta_file" .fasta)

    echo "🔁 Verarbeite $filename..."

    # Neues Arbeitsverzeichnis für dieses RNA-Modell
    work_dir="$OUTPUT_ROOT/$filename"
    mkdir -p "$work_dir"

    # seq.fasta in dieses Verzeichnis kopieren
    cp "$fasta_file" "$work_dir/seq.fasta"

    # DeepFoldRNA ausführen
    python3 "$DEEPFOLD_DIR/runDeepFoldRNA.py" \
        --input_dir "$work_dir" \
        --num_refinement_steps "$REFINE_STEPS"

    echo "✅ Fertig mit $filename. Ergebnisse in $work_dir"
done
