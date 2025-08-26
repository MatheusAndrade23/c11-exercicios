import numpy as np

dataset = np.loadtxt('./space.csv', delimiter=';', dtype="str", encoding='utf-8')

dados = dataset[1:]

empresas = dados[:, 1]

empresas_unicas, contagens = np.unique(empresas, return_counts=True)

print("Empresas e suas quantidades de missões:")
for empresa, quantidade in zip(empresas_unicas, contagens):
    print("Empresa: ", empresa, ", quantidade de missões: ", quantidade)