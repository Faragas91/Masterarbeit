import numpy as np
import matplotlib.pyplot as plt

# Read the file
timefile = open("D://Masterarbeit/Data/timings.txt", "r")
file = timefile.readlines()

# List of the tools
sissiz_mono = []
sissiz_di = []
multiperm_mono = []
multiperm_di = []
alifoldz = []

# Extract the Seconds in the empty lists
for i in file:
    if i.startswith("SISSIz_mono"):
        sissiz_mono.append(float(i.split()[5]))
    elif i.startswith("SISSIz_di"):
        sissiz_di.append(float(i.split()[5]))
    elif i.startswith("Multiperm_mono"):
        multiperm_mono.append(float(i.split()[5]))
    elif i.startswith("Multiperm_di"):
        multiperm_di.append(float(i.split()[5]))
    elif i.startswith("AliFoldz"):
        alifoldz.append(float(i.split()[5]))

########################################################################
########################################################################

# Box Plot
methods = {
    "SISSIz_mono": sissiz_mono,
    "SISSIz_di": sissiz_di,
    "Multiperm_mono": multiperm_mono,
    "Multiperm_di": multiperm_di,
    "AliFoldz": alifoldz,
}

plt.figure(figsize=(12, 8))

# Für jede Methode einen Subplot erstellen
for i, (name, data) in enumerate(methods.items(), start=1):
    plt.subplot(3, 2, i)
    plt.boxplot(data, patch_artist=True, showmeans=True, boxprops=dict(facecolor="skyblue"))
    plt.title(name, fontsize=12)
    plt.yscale("log")  # Logarithmische Skala
    plt.ylabel("Time (seconds)")
    plt.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()

################################################################
################################################################

# Bar Chart 1
# Average
mean_times = [
    np.mean(sissiz_mono),
    np.mean(sissiz_di),
    np.mean(multiperm_mono),
    np.mean(multiperm_di),
    np.mean(alifoldz),
]

# Maximum 
max_times = [
    np.max(sissiz_mono),
    np.max(sissiz_di),
    np.max(multiperm_mono),
    np.max(multiperm_di),
    np.max(alifoldz),
]

# Minimum
min_times = [
    np.min(sissiz_mono),
    np.min(sissiz_di),
    np.min(multiperm_mono),
    np.min(multiperm_di),
    np.min(alifoldz),
]

labels = ["SISSIz_mono", "SISSIz_di", "Multiperm_mono", "Multiperm_di", "AliFoldz"]

x = np.arange(len(labels))  
bar_width = 0.2  

plt.figure(figsize=(12, 6))
plt.bar(x - bar_width, mean_times, bar_width, label="Mean", color="skyblue")
plt.bar(x, max_times, bar_width, label="Max", color="orange")
plt.bar(x + bar_width, min_times, bar_width, label="Min", color="lightgreen")

# Layout
plt.ylabel("Time (seconds)", fontsize=12)
plt.xlabel("Methods", fontsize=12)
plt.title("Time to Generate Negative Samples", fontsize=14)
plt.xticks(x, labels, fontsize=10)
plt.legend(fontsize=10)
plt.grid(True, which="both", linestyle="--", linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()

################################################################
################################################################

# Bar Chart 2
# Total Time
total_times = [
    sum(sissiz_mono),
    sum(sissiz_di),
    sum(multiperm_mono),
    sum(multiperm_di),
    sum(alifoldz),
]

labels = ["SISSIz_mono", "SISSIz_di", "Multiperm_mono", "Multiperm_di", "AliFoldz"]

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, total_times, color=['skyblue', 'lightgreen', 'orange', 'pink', 'violet'])

for bar, total_time in zip(bars, total_times):
    plt.text(
        bar.get_x() + bar.get_width() / 2,  
        bar.get_height(),                 
        f"{total_time:.1f}",              
        ha="center", va="bottom",          
        fontsize=10, color="black"         
    )

plt.ylabel("Total Time (seconds)", fontsize=12)
plt.title("Total Time for Generating Negative Samples", fontsize=14)
plt.grid(axis='y', linestyle="--", linewidth=0.5, alpha=0.7)

plt.tight_layout()
plt.show()


# Scatter Plot
def plot_scatter(values, name):

        x = np.arange(len(values))

        # Plot erstellen
        plt.figure(figsize=(14, 8))
        plt.plot(x, values, marker='o', color='skyblue', label="Value progression")
        plt.scatter(x, values, color='darkblue', label="Individual values")

        # Achsentitel und Beschriftungen
        plt.title(name, fontsize=16)
        plt.xlabel("1000 negative Samples for 1 positiv Sample", fontsize=14)
        plt.ylabel("Time (seconds)", fontsize=14)

        # Gitternetz hinzufügen
        plt.grid(True, linestyle='--', alpha=0.7)

        # Legende anzeigen
        plt.legend(fontsize=12)

        # Plot anzeigen
        plt.tight_layout()
        plt.show()

# Scatter Plot für SISSIz_mono
plot_scatter(sissiz_mono, "SISSIz_mono",)

# Scatter Plot für SISSIz_di
plot_scatter(sissiz_di, "SISSIz_di")

# Scatter Plot für Multiperm_mono
plot_scatter(multiperm_mono, "Multiperm_mono")

# Scatter Plot für Multiperm_di
plot_scatter(multiperm_di, "Multiperm_di")

# Scatter Plot für AliFoldz
plot_scatter(alifoldz, "AliFoldz")








# print("SISSIz_mono Mean:" + str(np.mean(sissiz_mono)))
# print("SISSIz_mono Max:" + str(np.max(sissiz_mono)))
# print("SISSIz_mono Min:" + str(np.min(sissiz_mono)))

# print("SISSIz_di Mean:" + str(np.mean(sissiz_di)))
# print("SISSIz_di Max:" + str(np.max(sissiz_di)))
# print("SISSIz_di Min:" + str(np.min(sissiz_di)))

# print("multiperm_mono Mean:" + str(np.mean(multiperm_mono)))
# print("multiperm_mono Max:" + str(np.max(multiperm_mono)))
# print("multiperm_mono Min:" + str(np.min(multiperm_mono)))

# print("multiperm_di Mean:" + str(np.mean(multiperm_di)))
# print("multiperm_di Max:" + str(np.max(multiperm_di)))
# print("multiperm_di Min:" + str(np.min(multiperm_di)))

# print("AliFoldz Mean:" + str(np.mean(alifoldz)))
# print("AliFoldz Max:" + str(np.max(alifoldz)))
# print("AliFoldz Min:" + str(np.min(alifoldz)))