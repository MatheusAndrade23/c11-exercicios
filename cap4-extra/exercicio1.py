import numpy as np

dataset = np.loadtxt("./paises.csv", delimiter=";", dtype="str", encoding="utf-8")

dados = dataset[:, :4]

print(dados)