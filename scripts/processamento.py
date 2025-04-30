from trata_dados import Dados
import pandas as pd
import streamlit as st
import plotly.express as px

ano = 2024
local = f'data_raw/vendas{ano}.csv'

st.set_page_config(layout="wide")

df = Dados(local)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_cat = px.bar(df.catMaisVendida, x="category", y="quantity", title="Categorias Mais Vendidas")
col1.plotly_chart(fig_cat)

fig_mes = px.bar(df.receitaMensal, x="month", y="revenue", title="Receita Mensal")
col2.plotly_chart(fig_mes)

#fig_reg = px.pie(df.receitaRegiao, values="revenue", names="customer_region", title="Receita Por Região")
#col3.plotly_chart(fig_reg)