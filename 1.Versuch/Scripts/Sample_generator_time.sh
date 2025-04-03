#!/bin/bash

# Define variables
NEIGHBOURHOOD="/home/slais/Masterarbeit/neighbourhoods/bsubtilis401.nei"
TREE="/home/slais/Masterarbeit/trees/alina.tree"
ITER_POS=100
ITER_NEG=1000
TOTAL_FILES=$((500100))  # Total number of files to be processed
FREQUENCIES_SINGLE="0.422360 0.105590 0.236025 0.236025"
FREQUENCIES_DOUBLE="0.000423 0.004228 0.012685 0.169133 0.004228 0.000423 0.262156 0.000423 0.012685 0.262156 0.000423 0.042283 0.169133 0.000423 0.042283 0.016915"
SISSI="/home/slais/Masterarbeit/tools/sissi/sissi099"
SISSIz="/home/slais/Masterarbeit/tools/sissiz_v3/src/SISSIz"
RNAz="/home/slais/Masterarbeit/tools/RNAz-2.1.1/rnaz/RNAz"
ALIFOLDZ="/home/slais/Masterarbeit/tools/shuffle-aln.pl"  
MULTIPERM="/home/slais/Masterarbeit/tools/multiperm-0.9.4/multiperm" 
SAMPLES="/home/slais/Masterarbeit/SAMPLES"  
TMPDIR="/home/slais/Masterarbeit/tmp"  

# Make sure the executables have the necessary permissions
chmod +x "$SISSI"
chmod +x "$SISSIz"
chmod +x "$RNAz"
chmod +x "$MULTIPERM"

# Create the output directories if they don't exist
mkdir -p "$SAMPLES"
mkdir -p "$TMPDIR"

export TMPDIR

current_file=0

# Function to display the progress
function show_progress {
    local percentage=$(( current_file * 100 / TOTAL_FILES ))
    echo -ne "Progress: $percentage% ($current_file/$TOTAL_FILES) completed\r"
}

# Loop to generate samples
for i in $(seq 1 $ITER_POS); do
    SISSI_OUTPUT="$SAMPLES/pos_sample_output_$i.clu"
    
    if [ ! -f "$SISSI_OUTPUT" ]; then
        # Run the SISSI command to generate the SISSI sample
        "$SISSI" -fs $FREQUENCIES_SINGLE -fd $FREQUENCIES_DOUBLE -nn $NEIGHBOURHOOD -l401 $TREE -oc -d > $SISSI_OUTPUT
        echo "$SISSI finished"
    else 
        echo "$SISSI_OUTPUT already exists, skipping..."
    fi
    ((current_file++))
    show_progress

    # Started to generate 1000 SISSIz mononucleotide samples for each SISSI sample
    start_sissiz_mono=`date +%s.%N`
    # Inner loop to generate SISSIz mononucleotide samples 
    for z in $(seq 1 $ITER_NEG); do
        
        SISSIz_mono_OUTPUT="$SAMPLES/neg_sample_SISSIz_mono_output_${i}_${z}.clu"

        if [ ! -f "$SISSIz_mono_OUTPUT" ]; then
            # Run the SISSIz_mono command
            "$SISSIz" -s -i $SISSI_OUTPUT > $SISSIz_mono_OUTPUT
            echo "$SISSIz_mono_OUTPUT finished" 
        else 
            echo "$SISSIz_mono_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        show_progress
    done

    end_sissiz_mono=`date +%s.%N`
    runtime=$( echo "$end_sissiz_mono - $start_sissiz_mono" | bc -l )
    start_sissiz_mono=0
    end_sissiz_mono=0
    echo "SISSIz_mono for 1000 negativ Samples runtime: $runtime seconds"

    # Started to generate 1000 SISSIz dinucleotide samples for each SISSI sample
    start_sissiz_di=`date +%s.%N`
    # Inner loop to generate 10 SISSIz dinucleotide samples 
    for v in $(seq 1 $ITER_NEG); do
        SISSIz_di_OUTPUT="$SAMPLES/neg_sample_SISSIz_di_output_${i}_${v}.clu"

        if [ ! -f "$SISSIz_di_OUTPUT" ]; then
            # Run the SISSIz_di command
            "$SISSIz" -s $SISSI_OUTPUT > $SISSIz_di_OUTPUT
            echo "$SISSIz_di_OUTPUT finished"
        else 
            echo "$SISSIz_di_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        show_progress
    done

    end_sissiz_di=`date +%s.%N`
    runtime=$( echo "$end_sissiz_di - $start_sissiz_di" | bc -l )
    start_sissiz_di=0
    end_sissiz_di=0
    echo "SISSIz_di for 1000 negativ Samples runtime: $runtime seconds"

    # Started to generate 1000 Multiperm mononucleotide samples for each SISSI sample
    start_multiperm_mono=`date +%s.%N`
    # Inner loop to generate Multiperm mononucleotide samples
    for m in $(seq 1 $ITER_NEG); do
        MULTIPERM_mono_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_mono_output_${i}_${m}.clu"

        if [ ! -f "$MULTIPERM_mono_OUTPUT" ]; then
            # Run Multiperm command
            "$MULTIPERM" -w --conservation=none "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_mono_OUTPUT"
            echo "$MULTIPERM_mono_OUTPUT finished"
        else 
            echo "$MULTIPERM_mono_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        show_progress
    done
    
    end_multiperm_mono=`date +%s.%N`
    runtime=$( echo "$end_multiperm_mono - $start_multiperm_mono" | bc -l )
    start_multiperm_mono=0
    end_multiperm_mono=0
    echo "Mulitperm_mono for 1000 negativ Samples runtime: $runtime seconds"

    # Started to generate 1000 Multiperm dinucleotide samples for each SISSI sample
    start_multiperm_di=`date +%s.%N`
    # Inner loop to generate Multiperm dinucleotide samples
    for j in $(seq 1 $ITER_NEG); do
        MULTIPERM_di_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_di_output_${i}_${j}.clu"

        if [ ! -f "$MULTIPERM_di_OUTPUT" ]; then
            # Run Multiperm command
            "$MULTIPERM" -w "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_di_OUTPUT"
            echo "$MULTIPERM_di_OUTPUT finished"
        else 
            echo "$MULTIPERM_di_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        show_progress
    done

    end_multiperm_di=`date +%s.%N`
    runtime=$( echo "$end_multiperm_di - $start_multiperm_di" | bc -l )
    start_multiperm_di=0
    end_multiperm_di=0
    echo "Mulitperm_di for 1000 negativ Samples runtime: $runtime seconds"

    # Started to generate 1000 Alifoldz mononucleotide samples for each SISSI sample
    start_alifoldz=`date +%s.%N`
    # Inner loop to generate Alifoldz samples
    for k in $(seq 1 $ITER_NEG); do
        ALIFOLDz_OUTPUT="$SAMPLES/neg_sample_ALIFOLDz_output_${i}_${k}.clu"
        
        if [ ! -f "$ALIFOLDz_OUTPUT" ]; then
            # Run Alifoldz command
            perl "$ALIFOLDZ" < "$SISSI_OUTPUT" > "$ALIFOLDz_OUTPUT"
            echo "$ALIFOLDz_OUTPUT finished"
        else 
            echo "$ALIFOLDz_OUTPUT already exists, skipping..."
        fi
        ((current_file++))
        show_progress
    done

    end_alifoldz=`date +%s.%N`
    runtime=$( echo "$end_alifoldz - $start_alifoldz" | bc -l )
    start_alifoldz=0
    end_alifoldz=0
    echo "AliFoldz for 1000 negativ Samples runtime: $runtime seconds"
done

echo -ne "\nProcessing completed.\n"
