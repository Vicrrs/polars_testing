import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

# método que cria uma tabela pivô a partir de um DataFrame.
df_pivot = df.pivot(['idade'], ['satisfacao'], ['compras_ano_passado'])

# impressão do dataframe pivô
print(df_pivot)
