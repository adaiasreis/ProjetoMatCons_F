class ItemVenda():
    def __init__(self, quantidade, produto, preco_venda):
        self.quantidade = quantidade
        self.produto = produto
        self.preco_venda = preco_venda

    def getNomeProduto (self):
        return self.produto.nome
    
    def getValorUni(self):
        return self.produto.preco_venda

    def getValor(self):
        return "%.2f" % (float(self.produto.preco_venda) * float(self.quantidade))

    def novaQtd(self):
        return int("%.0f" % (int(self.produto.quantidade) - int (self.quantidade)))