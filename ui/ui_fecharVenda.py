from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp

from table.data_tableVenda import TableItens as Itens
from utils.venda import Venda
import models.vendas_model as Vendas

class FecharVenda(QWidget):
    def __init__(self, winCompra):
        super(). __init__()
        self.winCompra = winCompra
        uic.loadUi("ui/ui_fecharVenda.ui", self)

        self.painelValores()

        self.desconto = 0
        self.valorTotalP = 0
        self.TotalVenda = 0

    def setEventos(self):
        

        pass
    
    def painelValores(self):
        self.campTotalVenda.setText(self.winCompra.getValorTotal())
        """self.campDesconto.setText("%.2f" % self.desconto)
        self.campTotalPagar.setText("%.2f" % self.valorTotalP)"""

    """def finalizaVenda(self):
        #pega a data em string
        data = self.dateEdit.dateTime().toString('dd/MM/yyyy')
        cliente = self.clienteAtual
        lista_de_itens = self.tabelaItens.listaItens
        valor_total = (str(self.campValor_total.text()))
        # criado o objeto
        novaVenda = Venda(-1, cliente, lista_de_itens, valor_total, data)
        # armazenar no banco
        Vendas.addVenda(novaVenda)
        # limpar todos campos
        self.limparItens()"""
        
    """def closeEvent(self, event):
        self.winCompra.show()"""