import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4]))

data = df.loc[['A', 'C', 'E'], ['X', 'Y']]

print(data)

soma_por_linha = data.sum(axis=1)
print(soma_por_linha)

soma_por_coluna = data.sum(axis=0)
print(soma_por_coluna)