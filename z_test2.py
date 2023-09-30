import pandas as pd
from bioinfokit.analys import stat

# сбор данных и вывод первых 8 значений
df = pd.read_csv('Mall_Customers.csv', delimiter=',')
print(df.head(8))

res = stat()

res.ztest(df=df, x='Annual Income (k$)', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('Annual Income (k$)', res.summary, '\n\n', z, p)

res.ztest(df=df, x='Age', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('Age', res.summary, '\n\n', z, p)

res.ztest(df=df, x='Spending Score (1-100)', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('Spending Score (1-100)', res.summary, '\n\n', z, p)

