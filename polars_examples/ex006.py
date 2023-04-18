import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

print(df.head())
print(df.select("compras_ano_passado")) #método que seleciona colunas especificas de um DF
