import pandas as pd
from bioinfokit.analys import stat

# сбор данных и вывод первых 8 значений
df = pd.read_csv('winequality-white.csv', delimiter=';')
print(df.head(8))

res = stat()

res.ztest(df=df, x='quality', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('quality', res.summary, '\n\n', z, p)

res.ztest(df=df, x='alcohol', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('alcohol', res.summary, '\n\n', z, p)

res.ztest(df=df, x='sulphates', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('sulphates', res.summary, '\n\n', z, p)


res.ztest(df=df, x='citric acid', mu=5, x_std=0.4, test_type=1)
z, p = res.result[1], res.result[3]
print('citric acid', res.summary, '\n\n', z, p)


