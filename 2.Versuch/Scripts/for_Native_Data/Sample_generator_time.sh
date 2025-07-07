#!/bin/bash

# Define variables

SISSIz="/home/sredl/Masterarbeit/tools/sissiz_v3/src/SISSIz"
ALIFOLDZ="/home/sredl/Masterarbeit/tools/shuffle-aln.pl"  
MULTIPERM="/home/sredl/Masterarbeit/tools/multiperm-0.9.4/multiperm" 
SAMPLES_CLUSTAL="/home/sredl/Masterarbeit/2.Versuch/Native_Data/SAMPLES_CLUSTAL"  

# Make sure the executables have the necessary permissions
chmod +x "$SISSIz"
chmod +x "$MULTIPERM"

# Create the output directories if they don't exist
mkdir -p "$SAMPLES_CLUSTAL"

# Started to generate SISSIz mononucleotide samples
start_sissiz_mono=`date +%s.%N`

for z in "$SAMPLES_CLUSTAL"/*; do
    SISSIz_mono_OUTPUT="$SAMPLES_CLUSTAL/neg_sample_SISSIz_mono_${z}"

    if [ ! -f "$SISSIz_mono_OUTPUT" ]; then
        # Run the SISSIz_mono command
        "$SISSIz" -s -i $SISSI_OUTPUT > $SISSIz_mono_OUTPUT
        echo "$SISSIz_mono_OUTPUT finished" 
    else 
        echo "$SISSIz_mono_OUTPUT already exists, skipping..."
    fi
done

end_sissiz_mono=`date +%s.%N`
runtime=$( echo "$end_sissiz_mono - $start_sissiz_mono" | bc -l )
start_sissiz_mono=0
end_sissiz_mono=0
echo "SISSIz_mono runtime: $runtime seconds"


# Started to generate SISSIz dinucleotide samples for each SISSI sample
start_sissiz_di=`date +%s.%N`

# Inner loop to generate 10 SISSIz dinucleotide samples 
for v in "$SAMPLES_CLUSTAL"/*; do
    SISSIz_di_OUTPUT="$SAMPLES/neg_sample_SISSIz_di_${v}"

    if [ ! -f "$SISSIz_di_OUTPUT" ]; then
        # Run the SISSIz_di command
        "$SISSIz" -s $SISSI_OUTPUT > $SISSIz_di_OUTPUT
        echo "$SISSIz_di_OUTPUT finished"
    else 
        echo "$SISSIz_di_OUTPUT already exists, skipping..."
    fi
done

end_sissiz_di=`date +%s.%N`
runtime=$( echo "$end_sissiz_di - $start_sissiz_di" | bc -l )
start_sissiz_di=0
end_sissiz_di=0
echo "SISSIz_di runtime: $runtime seconds"


# Started to generate Multiperm mononucleotide samples for each SISSI sample
start_multiperm_mono=`date +%s.%N`

for m in "$SAMPLES_CLUSTAL"/*; do
    MULTIPERM_mono_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_mono_${m}"

    if [ ! -f "$MULTIPERM_mono_OUTPUT" ]; then
        # Run Multiperm command
        "$MULTIPERM" -w --conservation=none "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_mono_OUTPUT"
        echo "$MULTIPERM_mono_OUTPUT finished"
    else 
        echo "$MULTIPERM_mono_OUTPUT already exists, skipping..."
    fi
done

end_multiperm_mono=`date +%s.%N`
runtime=$( echo "$end_multiperm_mono - $start_multiperm_mono" | bc -l )
start_multiperm_mono=0
end_multiperm_mono=0
echo "Mulitperm_mono runtime: $runtime seconds"


# Started to generate Multiperm dinucleotide samples for each SISSI sample
start_multiperm_di=`date +%s.%N`

for j in "$SAMPLES_CLUSTAL"/*; do
    MULTIPERM_di_OUTPUT="$SAMPLES/neg_sample_MULTIPERM_di_${j}"

    if [ ! -f "$MULTIPERM_di_OUTPUT" ]; then
        # Run Multiperm command
        "$MULTIPERM" -w "$SISSI_OUTPUT" && mv perm_001_pos_sample_*.clu "$MULTIPERM_di_OUTPUT"
        echo "$MULTIPERM_di_OUTPUT finished"
    else 
        echo "$MULTIPERM_di_OUTPUT already exists, skipping..."
    fi
done

end_multiperm_di=`date +%s.%N`
runtime=$( echo "$end_multiperm_di - $start_multiperm_di" | bc -l )
start_multiperm_di=0
end_multiperm_di=0
echo "Mulitperm_di runtime: $runtime seconds"


# Started to generate 1000 Alifoldz mononucleotide samples for each SISSI sample
start_alifoldz=`date +%s.%N`

for k in "$SAMPLES_CLUSTAL"/*; do
    ALIFOLDz_OUTPUT="$SAMPLES/neg_sample_ALIFOLDz_${k}"
        
    if [ ! -f "$ALIFOLDz_OUTPUT" ]; then
        # Run Alifoldz command
        perl "$ALIFOLDZ" < "$SISSI_OUTPUT" > "$ALIFOLDz_OUTPUT"
        echo "$ALIFOLDz_OUTPUT finished"
    else 
        echo "$ALIFOLDz_OUTPUT already exists, skipping..."
    fi
done

end_alifoldz=`date +%s.%N`
runtime=$( echo "$end_alifoldz - $start_alifoldz" | bc -l )
start_alifoldz=0
end_alifoldz=0
echo "AliFoldz for 1000 negativ Samples runtime: $runtime seconds"

echo -ne "\nProcessing completed.\n"