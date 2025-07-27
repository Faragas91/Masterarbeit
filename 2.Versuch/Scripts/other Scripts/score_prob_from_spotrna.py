import numpy as np

def read_prob_file(filename):
    """
    Liest die SPOT-RNA .prob Datei ein und gibt eine numpy Matrix zurück.
    """
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    matrix = []
    for line in lines:
        # Zeile splitten, Filter für leere Strings, in float umwandeln
        row = [float(x) for x in line.strip().split() if x]
        matrix.append(row)
    
    return np.array(matrix)

def calculate_pairing_scores(prob_matrix):
    """
    Berechnet für jede Base die Summe der Paarungswahrscheinlichkeiten.
    Gibt auch den globalen Durchschnittswert zurück.
    """
    pairing_scores = np.sum(prob_matrix, axis=1)  # Summe pro Nukleotid
    global_score = np.mean(pairing_scores)        # Durchschnitt über alle Nukleotide
    return pairing_scores, global_score

if __name__ == "__main__":
    filename = "D:/Masterarbeit/2.Versuch/Result/Native_Results/SPOTRNA/6fz0-1-A.prob"  # Pfad zu deinem .prob File
    prob_matrix = read_prob_file(filename)
    
    pairing_scores, global_score = calculate_pairing_scores(prob_matrix)
    
    print(f"Globaler Pairing Confidence Score: {global_score:.4f}")
    print("Pairing Scores pro Position:", pairing_scores)

