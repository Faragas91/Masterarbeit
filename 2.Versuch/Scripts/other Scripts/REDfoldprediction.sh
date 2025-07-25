#!/bin/bash

SAMPLE_REDFOLD=/mnt/sdc2/home/c2210542009/Masterarbeit/Data/SAMPLES_REDFOLD
REDFOLD_PRE_OUTPUT=/mnt/sdc2/home/c2210542009/Masterarbeit/Data/REDFOLD_PREDICTION
METHODS=("ALIFOLDz" "MULTIPERM_MONO" "MULTIPERM_DI" "SISSIz_MONO" "SISSIz_DI" "POS_SAMPLES")
sample_sizes=(500 1000 1500 2000 2500 3000 3500 4000 4500 
5000 5500 6000 6500 7000 7500 8000 8500 9000 9500 10000 
10500 11000 11500 12000 12500 13000 13500 14000 14500 
15000 15500 16000 16500 17000 17500 18000 18500 19000 
19500 20000 20500 21000 21500 22000 22500 23000 23500 
24000 24500 25000 25500 26000 26500 27000 27500 28000 
28500 29000 29500 30000 30500 31000 31500 32000 32500 
33000 33500 34000 34500 35000 35500 36000 36500 37000 
37500 38000 38500 39000 39500 40000 40500 41000 41500 
42000 42500 43000 43500 44000 44500 45000 45500 46000 
46500 47000 47500 48000 48500 49000 49500 50000 50500 
51000 51500 52000 52500 53000 53500 54000 54500 55000 
55500 56000 56500 57000 57500 58000 58500 59000 59500 
60000 60500 61000 61500 62000 62500 63000 63500 64000 
64500 65000 65500 66000 66500 67000 67500 68000 68500 
69000 69500 70000 70500 71000 71500 72000 72500 73000 
73500 74000 74500 75000 75500 76000 76500 77000 77500 
78000 78500 79000 79500 80000 80500 81000 81500 82000 
82500 83000 83500 84000 84500 85000 85500 86000 86500 
87000 87500 88000 88500 89000 89500 90000 90500 91000 
91500 92000 92500 93000 93500 94000 94500 95000 95500 
96000 96500 97000 97500 98000 98500 99000 99500 100000)

mkdir -p "$REDFOLD_PRE_OUTPUT"

for method in "${METHODS[@]}"; do
    for size in "${sample_sizes[@]}"; do
        fasta_dir="${SAMPLE_REDFOLD}/${method}/${size}"
        if [[ -d "$fasta_dir" ]]; then
            echo "Running REDfold on directory $fasta_dir"
            output_file="$REDFOLD_PRE_OUTPUT/${method}_${size}.txt"
            lockfile="$output_file.lock"
            if ( set -o noclobber; echo "$$" > "$lockfile" ) 2> /dev/null; then
                if [[ -f "$output_file" ]]; then
                    echo "File ${method}_${size}.txt already exists"
                else
                    echo "Generate ${method}_${size}.txt"
                    redfold "$fasta_dir" > "$output_file"
                fi
                rm -f "$lockfile"
            else
                echo "Skipping ${method}_${size} – another process is working on it."
            fi
        fi
    done
done
