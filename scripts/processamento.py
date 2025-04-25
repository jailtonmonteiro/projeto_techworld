import pandas as pd

local = 'data_raw/vendas2024.csv'

#Extração
def carregaBase(local):
    df = pd.read_csv(local)
    df["order_date"] = pd.to_datetime(df["order_date"])
    df["month"] = df["order_date"].dt.month
    df["revenue"] = df["price"] * df["quantity"]
    return df

def categoriaVendida(df):
    categorias = df.groupby("category").agg({
        "quantity": "sum",
        "revenue": "sum"
    }).reset_index()
    categorias.columns = ["Categoria", "Quantidade_Vendas", "Valor_Total"]
    categorias["Valor_Total"] = categorias["Valor_Total"].apply(lambda x: f'R$ {x:,.2f}'.replace(",", "X").replace(".", ",").replace("X", "."))
    return categorias.sort_values(by="Quantidade_Vendas", ascending=False)


df = carregaBase(local)
print(categoriaVendida(df))