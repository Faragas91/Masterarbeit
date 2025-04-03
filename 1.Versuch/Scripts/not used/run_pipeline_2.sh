#!/bin/bash

# Define variables
NEIGHBOURHOOD="neighbourhoods/bsubtilis401.nei"
TREE="trees/alina.tree"
ITER_POS=100
ITER_NEG=1000
TOTAL_FILES=$((400100))  # Total number of files to be processed
FREQUENCIES_SINGLE="0.422360 0.105590 0.236025 0.236025"
FREQUENCIES_DOUBLE="0.000423 0.004228 0.012685 0.169133 0.004228 0.000423 0.262156 0.000423 0.012685 0.262156 0.000423 0.042283 0.169133 0.000423 0.042283 0.016915"
SISSI="/mnt/d/Masterarbeit/tools/sissi/sissi099"
SISSIz="/mnt/d/Masterarbeit/tools/sissiz_v3/src/SISSIz"
RNAz="/mnt/d/Masterarbeit/tools/RNAz-2.1.1/rnaz/RNAz"
ALIFOLDZ="/mnt/d/Masterarbeit/tools/shuffle-aln.pl"  
MULTIPERM="/mnt/d/Masterarbeit/tools/multiperm-0.9.4/multiperm" 
SAMPLES="/mnt/d/Masterarbeit/SAMPLES"  
SISSIz_PRE_OUTPUT="/mnt/d/Masterarbeit/SISSIz_PREDICTION"
RNAz_PRE_OUTPUT="/mnt/d/Masterarbeit/RNAz_PREDICTION"
TMPDIR="/mnt/d/Masterarbeit/tmp"  

# Make sure the executables have the necessary permissions
chmod +x "$SISSI"
chmod +x "$SISSIz"
chmod +x "$RNAz"
chmod +x "$MULTIPERM"

# Create the output directories if they don't exist
mkdir -p "$SAMPLES"
mkdir -p "$SISSIz_PRE_OUTPUT"
mkdir -p "$RNAz_PRE_OUTPUT"
mkdir -p "$TMPDIR"

export TMPDIR

current_file=0

# Function to display the progress
function show_progress {
    local percentage=$(( current_file * 100 / TOTAL_FILES ))
    echo -ne "Progress: $percentage% ($current_file/$TOTAL_FILES) completed\r"
}

# # Loop to generate samples
# for i in $(seq 1 $ITER_POS); do
#     SISSI_OUTPUT="$SAMPLES/pos_sample_output_$i.clu"
    
#     # Run the SISSI command to generate the SISSI sample
#     "$SISSI" -fs $FREQUENCIES_SINGLE -fd $FREQUENCIES_DOUBLE -nn $NEIGHBOURHOOD -l401 $TREE -oc -d > $SISSI_OUTPUT
#     ((current_file++))
#     show_progress

#     # # Inner loop to generate 10 SISSIz samples for each SISSI sample
#     # for u in $(seq 1 $ITER_NEG); do
#     #     SISSIz_OUTPUT="$SAMPLES/neg_sample_SISSIz_output_${i}_${u}.clu"
        
#     #     # Run the Multiperm command
#     #     "$SISSIz" -s $SISSI_OUTPUT > $SISSIz_OUTPUT
#     #     ((current_file++))
#     #     show_progress
#     # done

#     # Inner loop to generate 10 SISSIz mononucleotide samples for each SISSI sample
#     for z in $(seq 1 $ITER_NEG); do
#         SISSIz_mono_OUTPUT="$SAMPLES/neg_sample_SISSIz_mono_output_${i}_${z}.clu"
        
#         # Run the SISSIz_mono command
#         "$SISSIz" -s -i $SISSI_OUTPUT > $SISSIz_mono_OUTPUT
#         ((current_file++))
#         show_progress
#     done

#     # Inner loop to generate 10 SISSIz dinucleotide samples for each SISSI sample
#     for v in $(seq 1 $ITER_NEG); do
#         SISSIz_di_OUTPUT="$SAMPLES/neg_sample_SISSIz_di_output_${i}_${v}.clu"
        
#         # Run the SISSIz_di command
#         "$SISSIz" -s $SISSI_OUTPUT > $SISSIz_di_OUTPUT
#         ((current_file++))
#         show_progress
#     done
    
#     # Inner loop to generate Multiperm samples
#     for j in $(seq 1 $ITER_NEG); do
#         MULTIPERM_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_output_${i}_${j}.clu"
        
#         # Run Multiperm command
#         "$MULTIPERM" -w "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_OUTPUT"
#         ((current_file++))
#         show_progress
#     done
    
#     # Inner loop to generate Alifoldz samples
#     for k in $(seq 1 $ITER_NEG); do
#         ALIFOLDz_OUTPUT="$SAMPLES/neg_sample_ALIFOLDz_output_${i}_${k}.clu"
        
#         # Run Alifoldz command
#         perl "$ALIFOLDZ" < "$SISSI_OUTPUT" > "$ALIFOLDz_OUTPUT"
#         ((current_file++))
#         show_progress
#     done
# done

# # Run RNAz predictions for all samples
# for file in $SAMPLES/*.clu; do
#     basename=$(basename "$file" .clu)
#     output_file="$RNAz_PRE_OUTPUT/${basename}.txt"
    
#     # Check if output file already exists
#     if [ -f "$output_file" ]; then
#         echo "$output_file already exists, skipping..."
#         ((current_file++))
#         show_progress
#         continue
#     fi
    
#     # Run RNAz prediction
#     "$RNAz" -n "$file" >> "$output_file"
#     echo "$output_file finished"
#     ((current_file++))
#     show_progress
# done

# Run SISSIz predictions for all samples
for file in $SAMPLES/*.clu; do
    basename=$(basename "$file" .clu)
    output_file="$SISSIz_PRE_OUTPUT/${basename}.txt"

    # Check if output file already exists
    if [ -f "$output_file" ]; then
        echo "$output_file already exists, skipping..."
        ((current_file++))
        show_progress
        continue
    fi
    
    # Run SISSIz prediction
    "$SISSIz" --sci "$file" >> "$output_file"
    echo "$output_file finished"
    ((current_file++))
    show_progress
done


echo -ne "\nProcessing completed.\n"
