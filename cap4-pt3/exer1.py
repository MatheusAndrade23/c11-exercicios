import numpy as np

dataset = np.loadtxt('./space.csv', delimiter=';', dtype="str", encoding='utf-8')

dados = dataset[1:]

n_registros = dados.shape[0]

status_mission = dados[:, -1]

success_count = np.sum(status_mission == "Success")

print("Porcentagem: ", (success_count/n_registros)*100)