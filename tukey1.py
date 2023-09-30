import pandas as pd
import statsmodels. stats.multicomp as mc
import matplotlib.pyplot as plt

df = pd.read_csv('winequality-white.csv', delimiter=';')
print(df.head(8))

# Выполнить тест Тьюки
tukey = mc.MultiComparison(df['alcohol'], df['quality'])
result = tukey.tukeyhsd()
# Распечатать результаты
print(result)

# Выполнить тест Тьюки
tukey = mc.MultiComparison(df['sulphates'], df['citric acid'])
result = tukey.tukeyhsd()
# Распечатать результаты
print(result)
