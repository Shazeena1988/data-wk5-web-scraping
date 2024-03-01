import pandas as pd

df = pd.read_csv("results.csv")

# print(df.info())

# print(df.describe())

# print (df["home_score"].value_counts(normalize=True) * 100)

mask = df["home_score"] > 6
df = df[~mask]
print (df["home_score"].mean())