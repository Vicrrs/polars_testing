import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

# remoção das linhas duplicadas
df_unique = df.unique()

# impressão do dataframe sem as linhas duplicadas
print(df_unique)
