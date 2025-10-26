#!/bin/bash

# Define tools
SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm"
SAMPLES_CLUSTAL="/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_CLUSTAL_SUBFILES"
SAMPLES_MAF="/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_MAF"

chmod +x "$SISSIz"
chmod +x "$MULTIPERM"

mkdir -p "$SAMPLES_CLUSTAL"
mkdir -p "$SAMPLES_CLSTAL/positive"
mkdir -p "$SAMPLES_CLSTAL/negative"

start_all=$(date +%s.%N)
start_sissiz_mono=$(date +%s.%N)
echo "$start_sissiz_mono"

# Loop through each input .clu file
for input_file in "$SAMPLES_CLUSTAL/positive"/*.clu; do
# for input_file in "$SAMPLES_MAF"/*.maf; do
    filename=$(basename "$input_file")
    echo -e "\nProcessing: $filename"
    SISSIz_mono_out="$SAMPLES_CLUSTAL/negative/neg_sample_SISSIz_mono_${filename}"
    # SISSIz_mono_out="$SAMPLES_MAF/neg_sample_SISSIz_mono_${filename}"
    if [ ! -f "$SISSIz_mono_out" ]; then
        if timeout 10s "$SISSIz" -s -i "$input_file" > "$SISSIz_mono_out"; then
            echo "SISSIz mono done"
        else
            echo "⚠️  Timeout or error for $filename — skipping"
        fi
    else
        echo "SISSIz mono exists"
    fi
done

end_sissiz_mono=$(date +%s.%N)
runtime=$(echo "$end_sissiz_mono - $start_sissiz_mono" | bc -l)
echo -e "SISSIz mono completed in $runtime seconds.\n"

start_sissiz_di=$(date +%s.%N)
echo "$start_sissiz_di"

# Loop through each input .clu file
for input_file in "$SAMPLES_CLUSTAL/positive"/*.clu; do
    filename=$(basename "$input_file")
    echo -e "\nProcessing: $filename"
    SISSIz_di_out="$SAMPLES_CLUSTAL/negative/neg_sample_SISSIz_di_${filename}"
    # SISSIz_di_out="$SAMPLES_MAF/neg_sample_SISSIz_di_${filename}"
    if [ ! -f "$SISSIz_di_out" ]; then
        if timeout 10s "$SISSIz" -s -d "$input_file" > "$SISSIz_di_out"; then
            echo "SISSIz di done"
        else
            echo "⚠️  Timeout or error for $filename — skipping"
        fi
    else 
        echo "SISSIz di exists"
    fi
done

end_sissiz_di=$(date +%s.%N)
runtime=$(echo "$end_sissiz_di - $start_sissiz_di" | bc -l)
echo -e "SISSIz di completed in $runtime seconds.\n"

start_multiperm_mono=$(date +%s.%N)
echo "$start_multiperm_mono"

# Loop through each input .clu file
for input_file in "$SAMPLES_CLUSTAL/positive"/*.clu; do
    filename=$(basename "$input_file")
    echo -e "\nProcessing: $filename"
    MULTIPERM_mono_out="$SAMPLES_CLUSTAL/negative/neg_sample_MULTIPERM_mono_${filename}"
    # MULTIPERM_mono_out="$SAMPLES_MAF/neg_sample_MULTIPERM_mono_${filename}"
    if [ ! -f "$MULTIPERM_mono_out" ]; then
        if timeout 10s "$MULTIPERM" -w --conservation=none "$input_file"; then
            mv perm_001_*.clu "$MULTIPERM_mono_out" 2>/dev/null
            echo "MULTIPERM mono done"
        else
            echo "⚠️  Timeout or error for $filename — skipping"
        fi
    else
        echo "MULTIPERM mono exists"
    fi
done

end_multiperm_mono=$(date +%s.%N)
runtime=$(echo "$end_multiperm_mono - $start_multiperm_mono" | bc -l)
echo -e "MULTIPERM mono completed in $runtime seconds.\n"

start_multiperm_di=$(date +%s.%N)
echo "$start_multiperm_di"

# Loop through each input .clu file
for input_file in "$SAMPLES_CLUSTAL/positive"/*.clu; do
    filename=$(basename "$input_file")
    echo -e "\nProcessing: $filename"
    MULTIPERM_di_out="$SAMPLES_CLUSTAL/negative/neg_sample_MULTIPERM_di_${filename}"
    # MULTIPERM_di_out="$SAMPLES_MAF/neg_sample_MULTIPERM_di_${filename}"
    if [ ! -f "$MULTIPERM_di_out" ]; then
        if timeout 10s "$MULTIPERM" -w --conservation=level1 "$input_file"; then
            mv perm_001_*.clu "$MULTIPERM_di_out" 2>/dev/null
            echo "MULTIPERM di done"
        else
            echo "⚠️  Timeout or error for $filename — skipping"
        fi
    else
        echo "MULTIPERM di exists"
    fi
done

end_multiperm_di=$(date +%s.%N)
runtime=$(echo "$end_multiperm_di - $start_multiperm_di" | bc -l)
echo -e "MULTIPERM di completed in $runtime seconds.\n"

start_alifoldz=$(date +%s.%N)
echo "$start_alifoldz"

# Loop through each input .clu file
for input_file in "$SAMPLES_CLUSTAL/positive"/*.clu; do
    filename=$(basename "$input_file")
    echo -e "\nProcessing: $filename"
    ALIFOLDZ_out="$SAMPLES_CLUSTAL/negative/neg_sample_ALIFOLDz_${filename}"
    if [ ! -f "$ALIFOLDZ_out" ]; then
        if timeout 10s perl "$ALIFOLDZ" < "$input_file" > "$ALIFOLDZ_out"; then
            echo "ALIFOLDz done"
        else
            echo "⚠️  Timeout or error for $filename — skipping"
        fi
    else
        echo "ALIFOLDz exists"
    fi
done

end_alifoldz=$(date +%s.%N)
runtime=$(echo "$end_alifoldz - $start_alifoldz" | bc -l)
echo -e "ALIFOLDz completed in $runtime seconds.\n"

end_all=$(date +%s.%N)
runtime=$(echo "$end_all - $start_all" | bc -l)
echo -e "\nAll processing completed in $runtime seconds."
