import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4]))

linha_d = df.loc['D']
media_linha_d = linha_d.mean()

linha_e = df.iloc[4]
soma_linha_e = linha_e.sum()

print("Média dos elementos da linha D:", media_linha_d)
print("Soma dos elementos da linha E: ", soma_linha_e)