#!/bin/bash

# Define tools
SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm"
SAMPLES_CLUSTAL="/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_CLUSTAL"
SAMPLES_MAF="/home/sredl/Masterarbeit/2.Versuch/Native_Data/TEST_MAF"

chmod +x "$SISSIz"
chmod +x "$MULTIPERM"

start_all=$(date +%s.%N)

# Loop through each input .clu file
# for input_file in "$SAMPLES_CLUSTAL"/*.clu; do
for input_file in "$SAMPLES_MAF"/*.maf; do
    filename=$(basename "$input_file")

    echo -e "\nProcessing: $filename"

    ## ---------- SISSIz (mono) ----------
    # SISSIz_mono_out="$SAMPLES_CLUSTAL/neg_sample_SISSIz_mono_${filename}"
    SISSIz_mono_out="$SAMPLES_MAF/neg_sample_SISSIz_mono_${filename}"
    if [ ! -f "$SISSIz_mono_out" ]; then
        "$SISSIz" -s -i --maf "$input_file" > "$SISSIz_mono_out"
        echo "SISSIz mono done"
    else
        echo "SISSIz mono exists"
    fi

    ## ---------- SISSIz (di) ----------
    # SISSIz_di_out="$SAMPLES_CLUSTAL/neg_sample_SISSIz_di_${filename}"
    SISSIz_di_out="$SAMPLES_MAF/neg_sample_SISSIz_di_${filename}"
    if [ ! -f "$SISSIz_di_out" ]; then
        "$SISSIz" -s --maf "$input_file" > "$SISSIz_di_out"
        echo "SISSIz di done"
    else
        echo "SISSIz di exists"
    fi

    ## ---------- MULTIPERM (mono) ----------
    # MULTIPERM_mono_out="$SAMPLES_CLUSTAL/neg_sample_MULTIPERM_mono_${filename}"
    MULTIPERM_mono_out="$SAMPLES_MAF/neg_sample_MULTIPERM_mono_${filename}"
    if [ ! -f "$MULTIPERM_mono_out" ]; then
        # "$MULTIPERM" -w --conservation=none "$input_file"
        "$MULTIPERM" --conservation=none -v "$input_file"
        # mv perm_001_*.clu "$MULTIPERM_mono_out" 2>/dev/null
        mv perm_001_*.maf "$MULTIPERM_mono_out" 2>/dev/null
        echo "MULTIPERM mono done"
    else
        echo "MULTIPERM mono exists"
    fi

    ## ---------- MULTIPERM (di) ----------
    MULTIPERM_di_out="$SAMPLES_CLUSTAL/neg_sample_MULTIPERM_di_${filename}"
    if [ ! -f "$MULTIPERM_di_out" ]; then
        # "$MULTIPERM" -w "$input_file"
        "$MULTIPERM" --conservation=level1 -v "$input_file"
        # mv perm_001_*.clu "$MULTIPERM_di_out" 2>/dev/null
        mv perm_001_*.maf "$MULTIPERM_di_out" 2>/dev/null
        echo "MULTIPERM di done"
    else
        echo "MULTIPERM di exists"
    fi

    # ## ---------- ALIFOLDZ ----------
    # ALIFOLDZ_out="$SAMPLES_CLUSTAL/neg_sample_ALIFOLDz_${filename}"
    # if [ ! -f "$ALIFOLDZ_out" ]; then
    #     perl "$ALIFOLDZ" < "$input_file" > "$ALIFOLDZ_out"
    #     echo "ALIFOLDz done"
    # else
    #     echo "ALIFOLDz exists"
    # fi

done

end_all=$(date +%s.%N)
runtime=$(echo "$end_all - $start_all" | bc -l)
echo -e "\nAll processing completed in $runtime seconds."
#!/bin/bash

# Define tools
SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm"
SAMPLES_CLUSTAL="/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_CLUSTAL"
SAMPLES_MAF="/home/sredl/Masterarbeit/2.Versuch/Native_Data/TEST_MAF"

chmod +x "$SISSIz"
chmod +x "$MULTIPERM"

start_all=$(date +%s.%N)

# Loop through each input .clu file
# for input_file in "$SAMPLES_CLUSTAL"/*.clu; do
for input_file in "$SAMPLES_MAF"/*.maf; do
    filename=$(basename "$input_file")

    echo -e "\nProcessing: $filename"

    ## ---------- SISSIz (mono) ----------
    # SISSIz_mono_out="$SAMPLES_CLUSTAL/neg_sample_SISSIz_mono_${filename}"
    SISSIz_mono_out="$SAMPLES_MAF/neg_sample_SISSIz_mono_${filename}"
    if [ ! -f "$SISSIz_mono_out" ]; then
        "$SISSIz" -s -i "$input_file" > "$SISSIz_mono_out"
        echo "SISSIz mono done"
    else
        echo "SISSIz mono exists"
    fi

    ## ---------- SISSIz (di) ----------
    # SISSIz_di_out="$SAMPLES_CLUSTAL/neg_sample_SISSIz_di_${filename}"
    SISSIz_di_out="$SAMPLES_MAF/neg_sample_SISSIz_di_${filename}"
    if [ ! -f "$SISSIz_di_out" ]; then
        "$SISSIz" -s "$input_file" > "$SISSIz_di_out"
        echo "SISSIz di done"
    else
        echo "SISSIz di exists"
    fi

    ## ---------- MULTIPERM (mono) ----------
    # MULTIPERM_mono_out="$SAMPLES_CLUSTAL/neg_sample_MULTIPERM_mono_${filename}"
    MULTIPERM_mono_out="$SAMPLES_MAF/neg_sample_MULTIPERM_mono_${filename}"
    if [ ! -f "$MULTIPERM_mono_out" ]; then
        # "$MULTIPERM" -w --conservation=none "$input_file"
        "$MULTIPERM" --conservation=none "$input_file"
        # mv perm_001_*.clu "$MULTIPERM_mono_out" 2>/dev/null
        mv perm_001_*.maf "$MULTIPERM_mono_out" 2>/dev/null
        echo "MULTIPERM mono done"
    else
        echo "MULTIPERM mono exists"
    fi

    ## ---------- MULTIPERM (di) ----------
    MULTIPERM_di_out="$SAMPLES_MAF/neg_sample_MULTIPERM_di_${filename}"
    if [ ! -f "$MULTIPERM_di_out" ]; then
        # "$MULTIPERM" -w "$input_file"
        "$MULTIPERM" "$input_file"
        # mv perm_001_*.clu "$MULTIPERM_di_out" 2>/dev/null
        mv perm_001_*.maf "$MULTIPERM_di_out" 2>/dev/null
        echo "MULTIPERM di done"
    else
        echo "MULTIPERM di exists"
    fi

    # ## ---------- ALIFOLDZ ----------
    # ALIFOLDZ_out="$SAMPLES_CLUSTAL/neg_sample_ALIFOLDz_${filename}"
    # if [ ! -f "$ALIFOLDZ_out" ]; then
    #     perl "$ALIFOLDZ" < "$input_file" > "$ALIFOLDZ_out"
    #     echo "ALIFOLDz done"
    # else
    #     echo "ALIFOLDz exists"
    # fi

done

end_all=$(date +%s.%N)
runtime=$(echo "$end_all - $start_all" | bc -l)
echo -e "\nAll processing completed in $runtime seconds."
