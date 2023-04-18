import polars as pl

# criação do dataframe
df = pl.DataFrame({
    'idade': [36, 65, 65, 20, 66, 73, 73, 36, 31],
    'genero': ['Feminino', 'Feminino', 'Feminino', 'Masculino', 'Feminino', 'Feminino', 'Feminino', 'Feminino', 'Feminino'],
    'renda': [411.2659812347083, 1221.3917064243644, 1221.3917064243644, 3910.18673892502, 2349.845446239455, 3047.5059636381948, 1412.8491523708458, 3183.0041323566543, 2895.161032966609],
    'compras_ano_passado': [9, 4, 4, 2, 8, 6, 7, 2, 3],
    'satisfacao': ['Media', 'Baixa', 'Baixa', 'Baixa', 'Baixa', 'Media', 'Media', 'Baixa', 'Alta']
})

# encontra as linhas duplicadas
df_duplicates = df.groupby(['idade', 'genero', 'renda', 'compras_ano_passado', 'satisfacao'])\
                  .count()\
                  .filter(pl.col("count") > 1)\
                  .join(df, on=['idade', 'genero', 'renda', 'compras_ano_passado', 'satisfacao'])

# imprime as linhas duplicadas
print(df_duplicates)
