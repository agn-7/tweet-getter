import pandas as pd

__author__ = 'aGn'

df = pd.read_csv('../dataset/tweetIds.csv')
print(df.shape)

cleaned_df = df.dropna(how='any',axis=0)
print(cleaned_df.shape)

