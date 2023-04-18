import polars as pl

df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv")


print(df.fill_null()) # método que preenche valores nulos com um valor específico
