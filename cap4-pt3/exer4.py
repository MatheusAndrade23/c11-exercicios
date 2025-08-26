import numpy as np

dataset = np.loadtxt('./space.csv', delimiter=';', dtype="str", encoding='utf-8')

dados = dataset[1:]

empresas = dados[:, 1]
custos = dados[:, -2].astype(float)
missoes = dados[:, 4]

mascara_spacex = empresas == "SpaceX"

custos_spacex = custos[mascara_spacex]
missoes_spacex = missoes[mascara_spacex]

indice_max = np.argmax(custos_spacex)
missao_mais_cara = missoes_spacex[indice_max]
custo_max = custos_spacex[indice_max]

print("Missão mais cara: ", missao_mais_cara, " com o custo: ", custo_max)