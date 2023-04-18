import pandas as pd
import numpy as np

N = 10000
"""
O choice() método retorna um elemento selecionado aleatoriamente do especificado sequência.
O randint() método retorna um número inteiro número de elemento selecionado do intervalo especificado.
"""
data = {
    'idade': np.random.randint(18, 80, size=N),
    'genero':np.random.choice(['Masculino', 'Feminino'], size=N),
    'renda': np.random.normal(2500, 1000, size=N),
    'compras_ano_passado': np.random.randint(0, 10, size=N),
    'satisfacao': np.random.choice(['Baixa', 'Media', 'Alta'], size=N, p=[0.2, 0.6, 0.2])
}

df = pd.DataFrame(data)

df.to_csv('data.csv', index=False)
