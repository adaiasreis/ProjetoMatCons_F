from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from table.data_tableVenda import TableItens as Itens

class FecharVenda(QWidget):
    def __init__(self, winCompra):
        super(). __init__()
        self.winCompra = winCompra
        uic.loadUi("ui/ui_fecharVenda.ui", self)

        self.campDinheiro.textEdited.connect(self.text_edited)

        valorDinheiro = 0

        totalPagar = self.winCompra.campTotalPagar.text()
        if totalPagar == "":
            totalPagar = 0.0
        else:
           totalPagar = float(self.totalPagar)
            
        valorDinheiro = self.campDinheiro.text()
        if valorDinheiro == "":
            valorDinheiro = 0.0
        else:
            valorDinheiro = float(valorDinheiro)

        valorTroco = self.valorDinheiro - self.totalPagar


        self.campTotalPagar.setText("%.2f" % totalPagar)
        self.campDinheiro.setText("%.2f" % valorDinheiro)

    def text_edited(self, s):
        self.campTroco.setText("%.2f" % valorTroco)