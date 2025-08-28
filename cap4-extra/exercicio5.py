import numpy as np

dataset = np.loadtxt("./paises.csv", delimiter=";", encoding="utf-8", dtype="str")

dados = dataset[1:]

paises = dados[:, 0]
regions = dados[:, 1]
renda_percapita = dados[:, 8].astype(int)

mascara_caribe = np.char.startswith(regions, 'LATIN AMER. & CARIB')

renda_percapita_caribe = renda_percapita[mascara_caribe]
paises_caribe = paises[mascara_caribe]
indice_max = np.argmax(renda_percapita_caribe)

print("País com a maior renda per capita: ", paises_caribe[indice_max], ". Valor da renda: ", renda_percapita_caribe[indice_max])