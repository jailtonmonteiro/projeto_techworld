from trata_dados import Dados
import pandas as pd

local = 'data_raw/vendas2024.csv'

df = Dados(local)
print(df.exibir())