#!/bin/bash

# Define variables
ITER_NEG=100000
TOTAL_FILES=$((500000))  # Total number of files to be processed
SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"  
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm" 
NATIVE_SAMPLES="/home/sredl/Masterarbeit/Data/NATIVE_SAMPLES/"
NEGATIVE_SAMPLES="/home/sredl/Masterarbeit/Data/NEGATIVE_SAMPLES/"
POSITIVE_SAMPLES="$NATIVE_SAMPLES/bacillus_subtilis_Rfam.clu"

# Make sure the executables have the necessary permissions
chmod +x "$SISSIz"
chmod +x "$MULTIPERM"

mkdir -p "$NATIVE_SAMPLES"
mkdir -p "$NEGATIVE_SAMPLES"

current_file=0

# Function to display the progress
function show_progress {
    local percentage=$(( current_file * 100 / TOTAL_FILES ))
    echo -ne "Progress: $percentage% ($current_file/$TOTAL_FILES) completed\r"
}

#################################
########## SISSIz_mono ##########
#################################
file_step=0

    # Loop to generate 100000 SISSIz mononucleotide samples for each SISSI sample
    for z in $(seq 1 $ITER_NEG); do

        SISSIz_mono_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_SISSIz_mono_output_${z}.clu"

        if [ ! -f "$SISSIz_mono_OUTPUT" ]; then
            # Run the SISSIz_mono command
            "$SISSIz" -s -i $POSITIVE_SAMPLES > $SISSIz_mono_OUTPUT
            echo "$SISSIz_mono_OUTPUT finished" 
        else 
            echo "$SISSIz_mono_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

    if (( file_step % 1000 == 0 )); then
        timestamp=$(date +"%H:%M:%S")
        echo "SISSIz_mono: $file_step negative Samples finished at $timestamp"
        echo "SISSIz_mono: $file_step negative Samples finished at $timestamp" >> sissiz_mono_process.txt
    fi
    done

    #################################
    ########### SISSIz_di ###########
    #################################

    # Loop to generate 100000 SISSIz dinucleotide samples for each SISSI sample
    for v in $(seq 1 $ITER_NEG); do
        SISSIz_di_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_SISSIz_di_output_${v}.clu"

        if [ ! -f "$SISSIz_di_OUTPUT" ]; then
            # Run the SISSIz_di command
            "$SISSIz" -s $POSITIVE_SAMPLES > $SISSIz_di_OUTPUT
            echo "$SISSIz_di_OUTPUT finished"
        else 
            echo "$SISSIz_di_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if (( file_step % 1000 == 0 )); then
            timestamp=$(date +"%H:%M:%S")
            echo "SISSIz_di: $file_step negative Samples finished at $timestamp"
            echo "SISSIz_di: $file_step negative Samples finished at $timestamp" >> sissiz_di_process.txt
        fi
    done


    #################################
    ######## Multiperm_mono #########
    #################################

    # Loop to generate Multiperm mononucleotide samples
    for m in $(seq 1 $ITER_NEG); do
        MULTIPERM_mono_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_MULTIPERM_mono_output_${m}.clu"

        if [ ! -f "$MULTIPERM_mono_OUTPUT" ]; then
            # Run Multiperm command
            "$MULTIPERM" -w --conservation=none "$POSITIVE_SAMPLES" && mv perm_001_bacillus_subtilis_Rfam*.clu "$MULTIPERM_mono_OUTPUT"
            echo "$MULTIPERM_mono_OUTPUT finished"
        else 
            echo "$MULTIPERM_mono_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if (( file_step % 1000 == 0 )); then
            timestamp=$(date +"%H:%M:%S")
            echo "MULTIPERM_mono: $file_step negative Samples finished at $timestamp"
            echo "MULTIPERM_mono: $file_step negative Samples finished at $timestamp" >> multiperm_mono_process.txt
        fi
    done

    #################################
    ######### Multiperm_di ##########
    #################################

    # Loop to generate Multiperm dinucleotide samples
    for j in $(seq 1 $ITER_NEG); do
        MULTIPERM_di_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_MULTIPERM_di_output_${j}.clu"

        if [ ! -f "$MULTIPERM_di_OUTPUT" ]; then
            # Run Multiperm command
            "$MULTIPERM" -w "$POSITIVE_SAMPLES" && mv perm_001_bacillus_subtilis_Rfam*.clu "$MULTIPERM_di_OUTPUT"
            echo "$MULTIPERM_di_OUTPUT finished"
        else 
            echo "$MULTIPERM_di_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if (( file_step % 1000 == 0 )); then
            timestamp=$(date +"%H:%M:%S")
            echo "MULTIPERM_di: $file_step negative Samples finished at $timestamp"
            echo "MULTIPERM_di: $file_step negative Samples finished at $timestamp" >> multiperm_di_process.txt
        fi
    done

    #################################
    ######## aln-shuffle.pl #########
    #################################

    # Loop to generate Alifoldz samples
    for k in $(seq 1 $ITER_NEG); do
        ALIFOLDz_OUTPUT="$NEGATIVE_SAMPLES/neg_sample_ALIFOLDz_output_${k}.clu"
            
        if [ ! -f "$ALIFOLDz_OUTPUT" ]; then
            # Run Alifoldz command
            perl "$ALIFOLDZ" < "$POSITIVE_SAMPLES" > "$ALIFOLDz_OUTPUT"
            echo "$ALIFOLDz_OUTPUT finished"
        else 
            echo "$ALIFOLDz_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        ((file_step++))
        show_progress

        if (( file_step % 1000 == 0 )); then
            timestamp=$(date +"%H:%M:%S")
            echo "aln-shuffle: $file_step negative Samples finished at $timestamp"
            echo "aln-shuffle: $file_step negative Samples finished at $timestamp" >> aln_shuffle_process.txt
        fi
    done
echo -ne "\nProcessing completed.\n"
