import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#создание массива данных
df = pd.read_csv('Mall_Customers.csv', delimiter=',')

#функция нахождения iqr
def iqr(column):
    q75, q25 = np.percentile(df[column], [75, 25])
    iqr_result = q75 - q25
    print(column, '=', iqr_result)

#вывести данные и iqr каждого столбца
print(df.head(10), '\n')
iqr('Annual Income (k$)'), iqr('Age'), iqr('Spending Score (1-100)')

plt.figure(figsize=(10,5))
plt.subplot(2, 2, 1)
plt.scatter(df.index, df['Annual Income (k$)'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Annual Income (k$)')

plt.subplot(2, 2, 2)
plt.scatter(df.index, df['Age'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Age')

plt.subplot(2, 2, 3)
plt.scatter(df.index, df['Spending Score (1-100)'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Spending Score (1-100)')

plt.tight_layout()
plt.show()


