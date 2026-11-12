import pandas as pd

df = pd.read_csv(r"data\raw\student\student-mat.csv",sep=";")
print("number of rows and columns in the dataset:") 
print(df.shape)
print("values in the columns")
print(df.columns)
print("first few rows of the dataset:")
print(df.head())
print("data types of the columns:")
print(df.dtypes)
print("missing value:",df.isnull().sum().sum())

