import pandas as pd

df = pd.read_csv('./CleanedTeluguTrain.csv')

df = df.dropna(how='any')

mask = df['word'].str.match('^[a-zA-Z0-9 ]+$')
df = df[mask]

df.to_csv('telugutrain.csv', index=False)