import numpy as np

np.random.seed(10)

matriz = np.random.randint(1, 51, (4, 4))
print("Matriz: ", matriz)

media_linhas = matriz.mean(axis=1)
media_colunas = matriz.mean(axis=0)

print("Média das linhas: ", media_linhas)
print("Média das colunas: ", media_colunas)

maior_media_linhas = media_linhas.max()
maior_media_colunas = media_colunas.max()

print("Maior média das linhas: ", maior_media_linhas)
print("Maior média das colunas: ", maior_media_colunas)

valores, contagens = np.unique(matriz, return_counts=True)

print("Valores: ", valores)
print("Contagens: ", contagens)

numeros_2x = valores[contagens == 2]

print("Números que aparecem 2 vezes:", numeros_2x)