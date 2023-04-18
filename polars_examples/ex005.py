import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

df_nulos = df.null_count()

print(df_nulos) #verificando a presença de dados nulos
