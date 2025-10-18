#!/bin/bash

# Define variables
NEIGHBOURHOOD="/home/sredl/Masterarbeit/neighbourhoods/bsubtilis401.nei"
TREE="/home/sredl/Masterarbeit/trees/alina.tree"
ITER=100000
TOTAL_FILES=$(($ITER * 6))  # Total number of files to be processed
FREQUENCIES_SINGLE="0.422360 0.105590 0.236025 0.236025"
FREQUENCIES_DOUBLE="0.000423 0.004228 0.012685 0.169133 0.004228 0.000423 0.262156 0.000423 0.012685 0.262156 0.000423 0.042283 0.169133 0.000423 0.042283 0.016915"
SISSI="/home/sredl/Masterarbeit/tools/sissi/sissi099"
SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
RNAz="/home/sredl/Masterarbeit/tools/RNAz-2.1.1/rnaz/RNAz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"  
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm" 
SAMPLES="/home/sredl/Masterarbeit/2.Versuch/Data/SAMPLES"  
TMPDIR="/home/sredl/Masterarbeit/tmp"  

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
for i in $(seq 1 $ITER); do
    SISSI_OUTPUT="$SAMPLES/pos_sample_output_$i.clu"
    
    if [ ! -f "$SISSI_OUTPUT" ]; then
        # Run the SISSI command to generate the SISSI sample
        "$SISSI" -fs $FREQUENCIES_SINGLE -fd $FREQUENCIES_DOUBLE -nn $NEIGHBOURHOOD -l401 $TREE -oc > $SISSI_OUTPUT
        sleep $(shuf -i 1-2 -n 1)
        echo "$SISSI finished"
    else 
        echo "$SISSI_OUTPUT already exists, skipping..."
    fi
    ((current_file++))
    show_progress
done

# Started to generate SISSIz mononucleotide samples for each SISSI sample
start_sissiz_mono=`date +%s.%N`

for z in $(seq 1 $ITER); do
    SISSIz_mono_OUTPUT="$SAMPLES/neg_sample_SISSIz_mono_output_${z}.clu"

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
echo "SISSIz_mono runtime: $runtime seconds"


# Started to generate SISSIz dinucleotide samples for each SISSI sample
start_sissiz_di=`date +%s.%N`

# Inner loop to generate 10 SISSIz dinucleotide samples 
for v in $(seq 1 $ITER); do
    SISSIz_di_OUTPUT="$SAMPLES/neg_sample_SISSIz_di_output_${v}.clu"

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
echo "SISSIz_di runtime: $runtime seconds"


# Started to generate Multiperm mononucleotide samples for each SISSI sample
start_multiperm_mono=`date +%s.%N`

for m in $(seq 1 $ITER); do
    MULTIPERM_mono_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_mono_output_${m}.clu"

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
echo "Mulitperm_mono runtime: $runtime seconds"


# Started to generate Multiperm dinucleotide samples for each SISSI sample
start_multiperm_di=`date +%s.%N`

for j in $(seq 1 $ITER); do
    MULTIPERM_di_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_di_output_${j}.clu"

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
echo "Mulitperm_di runtime: $runtime seconds"


# Started to generate 1000 Alifoldz mononucleotide samples for each SISSI sample
start_alifoldz=`date +%s.%N`

for k in $(seq 1 $ITER); do
    ALIFOLDz_OUTPUT="$SAMPLES/neg_sample_ALIFOLDz_output_${k}.clu"
        
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

echo -ne "\nProcessing completed.\n"