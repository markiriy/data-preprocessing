import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#создание массива данных
df = pd.read_csv('winequality-white.csv', delimiter=';')

#функция нахождения iqr
def iqr(column):
    q75, q25 = np.percentile(df[column], [75, 25])
    iqr_result = q75 - q25
    print(column, '=', iqr_result)

#вывести данные и iqr каждого столбца
print(df.head(10), '\n')
iqr('quality'), iqr('alcohol'), iqr('sulphates'), iqr('citric acid')

plt.figure(figsize=(10,5))
plt.subplot(2, 2, 1)
plt.scatter(df.index, df['quality'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('quality')

plt.subplot(2, 2, 2)
plt.scatter(df.index, df['alcohol'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('alcohol')

plt.subplot(2, 2, 3)
plt.scatter(df.index, df['sulphates'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('sulphates')

plt.subplot(2, 2, 4)
plt.scatter(df.index, df['citric acid'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('citric acid')

plt.tight_layout()
plt.show()

