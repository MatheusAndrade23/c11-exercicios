import numpy as np

dataset = np.loadtxt("./paises.csv", delimiter=";", encoding="utf-8", dtype="str")

dados = dataset[1:]

regions = dados[:, 1]

unique_regions, counts = np.unique(regions, return_counts=True)

unique_regions_count = len(unique_regions)

print("Quantidade de regiões diferentes: ", len(unique_regions))
for c in range(unique_regions_count):
    print("Região: ", unique_regions[c], ", quantidade que aparece: ", counts[c], " vezes")