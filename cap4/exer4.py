import numpy as np

matriz = np.array([[1, 2, 3, 4], 
                   [5, 6, 7, 8], 
                   [9, 10, 11, 12]])

linhas, colunas = matriz.shape

total_elementos = linhas * colunas

if total_elementos % 2 == 0:
    tipo = "par"
else:
    tipo = "ímpar"


print("Matriz original:")
print(matriz)
print("Número de linhas: {linhas}")
print("Número de colunas: {colunas}")
print("Essa matriz poderia se tornar um vetor unidimensional com número {tipo} de elementos.")

