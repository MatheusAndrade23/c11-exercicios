import pandas as pd

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

diffAno2Ano1 = seriesAno2 - seriesAno1

seriesAno3 = seriesAno2 + diffAno2Ano1
seriesAno4 = seriesAno3 + diffAno2Ano1

print(seriesAno4.nlargest(1))