from trata_dados import Dados
import pandas as pd

ano = int(input('Digite o ano que deseja ver o relatório: '))
local = f'data_raw/vendas{ano}.csv'

df = Dados(local)
print(df.exibir())