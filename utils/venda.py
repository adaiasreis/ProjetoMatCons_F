class Venda():
    def __init__(self, id, cliente, lista_de_itens, valor_total, data):
        self.id = id
        self.cliente = cliente
        self.lista_de_itens = lista_de_itens
        self.valor_total = valor_total
        self.data = data

    # quantidade de itens no carrinho
    def qtdItens(self):
        return len(self.lista_de_itens)
    
    # lista de itens
    def getItens(self):
        return self.lista_de_itens
    
    def getValorTotal(self):
        return self.valor_total