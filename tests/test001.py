import polars as pl


df = pl.read_csv("/home/rozatk/PythonProjects/Test_Polars/archives/data.csv").filter(
     (pl.col('idade') == 19) &
     (pl.col('genero') == 'Feminino'))

count = df.height
print(count)
