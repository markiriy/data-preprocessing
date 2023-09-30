import pandas as pd
import statsmodels. stats.multicomp as mc

df = pd.read_csv('Mall_Customers.csv', delimiter=',')
print(df.head(8))

# Выполнить тест Тьюки
tukey = mc.MultiComparison(df['Annual Income (k$)'], df['Age'])
result = tukey.tukeyhsd()
# Распечатать результаты
print(result)

# Выполнить тест Тьюки
tukey = mc.MultiComparison(df['Spending Score (1-100)'], df['Age'])
result = tukey.tukeyhsd()
# Распечатать результаты
print(result)
