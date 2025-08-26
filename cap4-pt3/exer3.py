import numpy as np

dataset = np.loadtxt('./space.csv', delimiter=';', dtype="str", encoding='utf-8')

dados = dataset[1:]

localizacoes = dados[:, 2]

mascara_usa = np.char.endswith(localizacoes, "USA")
total_usa = np.sum(mascara_usa)


print(total_usa)