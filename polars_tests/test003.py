import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

# encontra as linhas duplicadas
df_duplicates = df.groupby(['idade', 'genero', 'renda', 'compras_ano_passado', 'satisfacao'])\
                  .count()\
                  .filter(pl.col("count") > 1)\
                  .join(df, on=['idade', 'genero', 'renda', 'compras_ano_passado', 'satisfacao'])

# imprime as linhas duplicadas
print(df_duplicates)
