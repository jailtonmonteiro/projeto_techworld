import pandas as pd

class Dados:
    def __init__(self, local):
        self.local = local
        self.df = self.__trataData()
        self.catMaisVendida = self.__categoriasVendidas()
        self.ticketM = self.__ticketMedio()
        self.receitaMensal = self.__receitaMes()
        self.receitaRegiao = self.__receitaReg()
        self.pagamentoUsado = self.__metodoPag()
        self.maisVendido = self.__maisVend()

    # Carrega a base de dados
    def __carregaBase(self):
        df = pd.read_csv(self.local)
        return df
    
    # Altera formato do campo date, separa os meses e cria coluna com valor total de cada pedido
    def __trataData(self):
        df = self.__carregaBase()
        # Altera o campo de data para formato datetime
        df["order_date"] = pd.to_datetime(df["order_date"])
        # Cria coluna de meses
        df["month"] = df["order_date"].dt.month
        # Cria coluna com o valor total de cada pedido
        df["revenue"] = df["price"] * df["quantity"]
        return df

    # Exibe as categorias mais vendidas
    def __categoriasVendidas(self):
        cat = self.df.groupby("category", as_index=False)["quantity"].sum()
        cat = cat.sort_values(by="quantity", ascending=False)
        # Incluindo o percentual que cada categoria representa
        cat["percentual"] = (cat["quantity"] / cat["quantity"].sum()) * 100
        cat["percentual"] = cat["percentual"].round(1) # Arredonda para 1 casa decimal
        return cat

    # Calcula o ticket médio dos pedidos
    def __ticketMedio(self):
        tm = self.df["revenue"].sum() / self.df["order_id"].nunique()
        return tm.round(2)
    
    #Verifica a evolução das receitas ao longo dos meses
    def __receitaMes(self):
        recMes = self.df.groupby("month")["revenue"].sum()
        return recMes
    
    # Descobrir regiões que mais compraram
    def __receitaReg(self):
        recReg = self.df.groupby("customer_region")["revenue"].sum().sort_values(ascending=False)
        return recReg
    
    # Determinar os métodos de pagamento mais utilizados
    def __metodoPag(self):
        metPag = self.df["payment_method"].value_counts().sort_values(ascending=False)
        return metPag
    
    # Apontar o produto campeão de vendas
    def __maisVend(self):
        maisV = self.df.groupby("product_name")["quantity"].sum().head(1)
        return maisV
    
    # Facilita exibição
    @staticmethod
    def __facilitaExibicao(titulo):
        print('--'*20)
        print(f'{titulo:^40}')
        print('--'*20)
    
    def exibir(self):
        self.__facilitaExibicao('Categoria Mais Vendida')
        print(self.catMaisVendida)
        self.__facilitaExibicao('Ticket Médio das Vendas')
        print(f'R$ {self.ticketM}')
        self.__facilitaExibicao('Receita Mês a Mês')
        print(self.receitaMensal)
        self.__facilitaExibicao('Receita Por Região')
        print(self.receitaRegiao)
        self.__facilitaExibicao('Pagamentos Mais Utilizados')
        print(self.pagamentoUsado)
        self.__facilitaExibicao('Produto Mais Vendido')
        print(self.maisVendido)