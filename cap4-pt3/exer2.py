import numpy as np

dataset = np.loadtxt('./space.csv', delimiter=';', dtype="str", encoding='utf-8')

dados = dataset[1:]

custos = dados[:, -2]
custos_numericos = custos.astype("float")

custos_maiores_que_zero = custos_numericos[custos_numericos > 0]
soma_custos_tratado = np.sum(custos_maiores_que_zero)

n_regitros_tratado = np.count_nonzero(custos_numericos > 0)

print("Media: ", soma_custos_tratado/n_regitros_tratado)