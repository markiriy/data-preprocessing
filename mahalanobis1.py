import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# функция вычисления расстояния Махаланобиса
def calculateMahalanobis(y=None, data=None, cov=None):
    y_mu = y - np.mean(data)
    if not cov:
        cov = np.cov(data.values.T)
    inv_covmat = np.linalg.inv(cov)
    left = np.dot(y_mu, inv_covmat)
    mahal = np.dot(left, y_mu.T)
    return mahal.diagonal()


# реальные данные
data =  pd.read_csv('winequality-white.csv', delimiter=';')

# создание датасета
df = pd.DataFrame(data, columns=['quality', 'alcohol', 'sulphates',
                                 'citric acid'])

# создание нового элемента в датафрейме, который будет держать расстояние Махаланобиса для каждой строки
df['Mahalanobis'] = calculateMahalanobis(y=df, data=df[[
    'quality', 'alcohol', 'sulphates',
    'citric acid']])

# вывод датафрейма
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.max_colwidth', None,
                       ):
    print(df)

plt.figure(figsize=(10,5))

plt.scatter(df.index, df['Mahalanobis'], alpha=0.8, s=80)
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Mahalanobis')

plt.show()
