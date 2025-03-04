#!/bin/bash

# Define variables
ITER_NEG=100000
TOTAL_FILES=$((500000))  # Total number of files to be processed
SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"  
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm" 
NEGATIVE_SAMPLES="/home/sredl/Masterarbeit/NEGATIVE_SAMPLES"  
NATIVE_SAMPLES="/home/sredl/Masterarbeit/native_samples.clu"

# Make sure the executables have the necessary permissions
chmod +x "$SISSIz"
chmod +x "$MULTIPERM"

# Create the output directories if they don't exist
mkdir -p "$NEGATIVE_SAMPLES"  

current_file=0

# Function to display the progress
function show_progress {
    local percentage=$(( current_file * 100 / TOTAL_FILES ))
    echo -ne "Progress: $percentage% ($current_file/$TOTAL_FILES) completed\r"
}

for i in "$NATIVE_SAMPLES"; do

#################################
########## SISSIz_mono ##########
#################################

    # Loop to generate 100000 SISSIz mononucleotide samples for each SISSI sample
    for z in $(seq 1 $ITER_NEG); do
        file_step=0
        SISSIz_mono_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_SISSIz_mono_output_${i}_${z}.clu"

        if [ ! -f "$SISSIz_mono_OUTPUT" ]; then
            # Run the SISSIz_mono command
            "$SISSIz" -s -i $SISSI_OUTPUT > $SISSIz_mono_OUTPUT
            echo "$SISSIz_mono_OUTPUT finished" 
        else 
            echo "$SISSIz_mono_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if [ "$file_step" -eq 1000 ]; then
            timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            echo "SISSIz_mono for 1000 negativ Samples runtime: $timestamp seconds"
            file_step=0
        fi
    done

    #################################
    ########### SISSIz_di ###########
    #################################

    # Loop to generate 100000 SISSIz dinucleotide samples for each SISSI sample
    for v in $(seq 1 $ITER_NEG); do
        file_step=0
        SISSIz_di_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_SISSIz_di_output_${i}_${v}.clu"

        if [ ! -f "$SISSIz_di_OUTPUT" ]; then
            # Run the SISSIz_di command
            "$SISSIz" -s $SISSI_OUTPUT > $SISSIz_di_OUTPUT
            echo "$SISSIz_di_OUTPUT finished"
        else 
            echo "$SISSIz_di_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if [ "$file_step" -eq 1000 ]; then
            timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            echo "SISSIz_di for 1000 negativ Samples runtime: $timestamp seconds"
            file_step=0
        fi
    done


    #################################
    ######## Multiperm_mono #########
    #################################

    # Loop to generate Multiperm mononucleotide samples
    for m in $(seq 1 $ITER_NEG); do
        file_step=0
        MULTIPERM_mono_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_MULTIPERM_mono_output_${i}_${m}.clu"

        if [ ! -f "$MULTIPERM_mono_OUTPUT" ]; then
            # Run Multiperm command
            "$MULTIPERM" -w --conservation=none "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_mono_OUTPUT"
            echo "$MULTIPERM_mono_OUTPUT finished"
        else 
            echo "$MULTIPERM_mono_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if [ "$file_step" -eq 1000 ]; then
            timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            echo "Multiperm_mono for 1000 negativ Samples runtime: $timestamp seconds"
            file_step=0
        fi
    done

    #################################
    ######### Multiperm_di ##########
    #################################

    # Loop to generate Multiperm dinucleotide samples
    for j in $(seq 1 $ITER_NEG); do
        file_step=0
        MULTIPERM_di_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_MULTIPERM_di_output_${i}_${j}.clu"

        if [ ! -f "$MULTIPERM_di_OUTPUT" ]; then
            # Run Multiperm command
            "$MULTIPERM" -w "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_di_OUTPUT"
            echo "$MULTIPERM_di_OUTPUT finished"
        else 
            echo "$MULTIPERM_di_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if [ "$file_step" -eq 1000 ]; then
            timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            echo "Multiperm_di for 1000 negativ Samples runtime: $timestamp seconds"
            file_step=0
        fi
    done

    #################################
    ######## aln-shuffle.pl #########
    #################################

    # Loop to generate Alifoldz samples
    for k in $(seq 1 $ITER_NEG); do
        file_step=0
        ALIFOLDz_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_ALIFOLDz_output_${i}_${k}.clu"
            
        if [ ! -f "$ALIFOLDz_OUTPUT" ]; then
            # Run Alifoldz command
            perl "$ALIFOLDZ" < "$SISSI_OUTPUT" > "$ALIFOLDz_OUTPUT"
            echo "$ALIFOLDz_OUTPUT finished"
        else 
            echo "$ALIFOLDz_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if [ "$file_step" -eq 1000 ]; then
            timestamp=$(date +"%Y-%m-%d %H:%M:%S")
            echo "aln-shuffle for 1000 negativ Samples runtime: $timestamp seconds"
            file_step=0
        fi
    done

echo -ne "\nProcessing completed.\n"
