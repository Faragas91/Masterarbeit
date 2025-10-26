#!/bin/bash

# URL zur Datei
URL="ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nt.gz"
MD5_EXPECTED="bf9c9ff771b39cfbb875ea81c10ab789" 

# Lade mit Resume-Funktion
echo "🟡 Starte oder setze Download fort..."
wget -c "$URL"

# Prüfe, ob Datei komplett ist (Dateigröße > 377 GB)
MIN_SIZE=$((377 * 1024 * 1024 * 1024))  # ~377 GB in Bytes
ACTUAL_SIZE=$(stat -c %s "nt.gz")

if [ "$ACTUAL_SIZE" -lt "$MIN_SIZE" ]; then
    echo "🔴 Datei ist zu klein – möglicherweise unvollständig."
    echo "   Aktuell: $(du -h nt.gz)"
    exit 1
fi

# Prüfe MD5-Hash
echo "🧪 Prüfe MD5-Checksumme..."
MD5_ACTUAL=$(md5sum nt.gz | awk '{print $1}')

if [ "$MD5_ACTUAL" == "$MD5_EXPECTED" ]; then
    echo "✅ Alles gut! nt.gz wurde korrekt heruntergeladen."
else
    echo "❌ MD5 stimmt nicht überein!"
    echo "   Erwartet: $MD5_EXPECTED"
    echo "   Tatsächlich: $MD5_ACTUAL"
    echo "   → Datei ist vermutlich beschädigt."
    exit 1
fi
