from trata_dados import Dados
import pandas as pd
import streamlit as st
import plotly.express as px

ano = 2022
local = f'data_raw/vendas{ano}.csv'

st.set_page_config(
    layout="wide",
    page_icon="📊",
    page_title="TechWorld Insights"
    )

df = Dados(local)

col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

fig_cat = px.bar(df.catMaisVendida, x="category", y="quantity", title="Categorias Mais Vendidas")
col1.plotly_chart(fig_cat)

fig_mes = px.bar(df.receitaMensal, x="month", y="revenue", title="Receita Mensal")
col2.plotly_chart(fig_mes)

fig_reg = px.pie(df.receitaRegiao.reset_index(), values="revenue", names="customer_region", title="Receita Por Região")
col3.plotly_chart(fig_reg)

col4.markdown(f"""
    <div style="background-color:#0e1117; padding:30px; border-radius:10px; text-align:center">
        <h4 style="color:white;">Ticket Médio</h4>
        <h1 style="color:#39ff14;">R$ {df.ticketM}</h1>
    </div>
""", unsafe_allow_html=True)


fig_pay = px.pie(df.pagamentoUsado.reset_index(), values="count", names="payment_method", title="Pagamentos Mais Utilizados")
col5.plotly_chart(fig_pay)