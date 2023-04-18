import polars as pl

df_pessoas = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/pessoas.csv")

df_compras = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/compras.csv")

# junção dos dataframes utilizando a coluna 'genero' como chave de junção
df_joined = df_pessoas.join(df_compras, on='genero')

# impressão do dataframe resultante da junção
print(df_joined)
