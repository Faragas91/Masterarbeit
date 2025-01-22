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


# Bar Chart
# Average
mean_times = [
    np.mean(sissiz_mono),
    np.mean(sissiz_di),
    np.mean(multiperm_mono),
    np.mean(multiperm_di),
    np.mean(alifoldz),
]

max_times = [
    np.max(sissiz_mono),
    np.max(sissiz_di),
    np.max(multiperm_mono),
    np.max(multiperm_di),
    np.max(alifoldz),
]

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