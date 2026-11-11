import pandas as pd

df = pd.read_csv(r"data\raw\student\student-mat.csv",sep=";")
print(df.shape)
print(df.columns)
print(df.head())
print(df.dtypes)
print(df.isnull().sum().sum())