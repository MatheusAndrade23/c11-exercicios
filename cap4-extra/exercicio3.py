import numpy as np

dataset = np.loadtxt("./paises.csv", delimiter=";", encoding="utf-8", dtype="str")

dados = dataset[1:]

literacy = dados[:, 9].astype(float)

print("Média: ", np.mean(literacy))
