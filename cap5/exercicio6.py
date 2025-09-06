import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4]))

coluna_x = df['X']
coluna_x_menores_que_30 = coluna_x[coluna_x < 30]

print("Média dos elementos da coluna X que são menores que 30: ", coluna_x_menores_que_30.mean())