import pandas as pd
import numpy as np

indices = ["a", "b", "c", "e"]
valores = [1, 2, 3, 4]

dict = {"a": 10, "b": 20, "c": 30, "d": 40}

series = pd.Series(dict)
series2 = pd.Series(index=indices, data=valores)

print(series.add(series2, fill_value=0))

print(series[series <= 20])

df = pd.DataFrame(
        index=['A', 'B', 'C', 'D'],
        columns=['W', 'X', 'Y', 'Z'],
        data=np.random.randint(1, 50, [4, 4])
    )

print(df.iloc[0:2, :])
print(df.loc[['A', 'B'], ['W', 'X', 'Y', 'Z']])