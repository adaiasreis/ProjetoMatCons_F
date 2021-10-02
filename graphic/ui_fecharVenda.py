from PyQt5.QtWidgets import QWidget
from PyQt5 import uic

from table.data_tableVenda import TableItens as Itens

class FecharVenda(QWidget):
    def __init__(self, winCompra):
        super(). __init__()
        self.winCompra = winCompra
        uic.loadUi("ui/ui_fecharVenda.ui", self)

        #self.campDinheiro.setPlaceholderText(self.campDinheiro)
        self.totalPagar = self.winCompra.campTotalPagar.text()
        self.campTotalPagar.setText(self.totalPagar)
        

        self.campDinheiro.textEdited.connect(self.text_edited)

    def text_edited(self, valorDinheiro):
        print(valorDinheiro)

        valorTroco = 0

        if valorDinheiro != "":
    
            if float(self.totalPagar) < float(valorDinheiro):

                valorTroco = float(valorDinheiro) - float(self.totalPagar)

            self.campTroco.setText("%.2f" % valorTroco)