import numpy as np

dataset = np.loadtxt("./paises.csv", delimiter=";", encoding="utf-8", dtype="str")

dados = dataset[1:]
regions = dados[:, 1]

total_america_norte = np.sum(np.char.startswith(regions, 'NORTHERN AMERICA'))

print(total_america_norte)