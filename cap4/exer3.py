import numpy as np
import random

campo = np.array([[0, 0], [0, 0]])

linha_aleatoria = random.randint(0, campo.shape[0] - 1)
coluna_aleatoria = random.randint(0, campo.shape[1] - 1)
campo[linha_aleatoria, coluna_aleatoria] = 1

print("Campo Minado! Faça suas jogadas!")

n_jogadas = 0

while(1):

    if(n_jogadas == 3):
        print("Congratulations! You beat the game! :)")
        break

    linha = int(input("Escolha uma linha do campo (1 ou 2): "))
    coluna = int(input("Escolha uma coluna do campo (1 ou 2): "))

    if(campo[linha -1][coluna - 1] == 1):
        print("Game Over! :( Try Again")
        break

    print("Mais uma jogada!")