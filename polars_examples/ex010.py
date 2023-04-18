import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

# ordenação pelo campo 'compras_ano_passado' de forma decrescente
# método que ordena as linhas de um DataFrame de acordo com uma ou mais colunas.
df_sorted = df.sort('compras_ano_passado')

# impressão do dataframe ordenado
print(df_sorted)
