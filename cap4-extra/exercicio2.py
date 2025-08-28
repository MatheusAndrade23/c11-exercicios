import numpy as np

dataset = np.loadtxt("./paises.csv", delimiter=";", encoding="utf-8", dtype="str")

dados = dataset[1:]

regions = dados[:, 1]

unique_regions = np.unique(regions)

unique_regions_count = len(unique_regions)

print("Quantidade de regiões diferentes: ", len(unique_regions))
print(unique_regions)