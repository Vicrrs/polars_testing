import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")

condicao = df["renda"].sum() > 10

df_filtrado = df.filter(condicao) #O método .filter() retorna um novo DataFrame contendo apenas as linhas que atendem à condição especificada

print(df_filtrado)
