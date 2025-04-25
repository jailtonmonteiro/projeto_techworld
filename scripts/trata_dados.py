import pandas as pd

class Dados:
    def __init__(self, local):
        self.local = local
        self.df = self.trataData()

    def __carregaBase(self):
        df = pd.read_csv(self.local)
        return df
    
    def trataData(self):
        df = self.__carregaBase()
        # Altera o campo de data para formato datetime
        df["order_date"] = pd.to_datetime(df["order_date"])
        # Cria coluna de meses
        df["month"] = df["order_date"].dt.month
        # Cria coluna com o valor total de cada pedido
        df["revenue"] = df["price"] * df["quantity"]
        return df
    
    def exibir(self):
        return self.df