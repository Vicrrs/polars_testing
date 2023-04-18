import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

# método que agrupa linhas de um DataFrame de acordo com os valores em uma ou mais colunas.
df_agrupado = df.groupby(["genero", "idade"])

# Calcular a média das colunas numéricas para cada grupo
df_media = df_agrupado.count()

print(df_media) 
