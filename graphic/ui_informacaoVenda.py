from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton

from PyQt5 import uic
from PyQt5.QtCore import Qt

class InfoVenda(QWidget):
    def __init__(self, venda):
        super().__init__()
        uic.loadUi("ui/ui_informacaoVenda.ui", self)

        self.venda = venda

        self.campCliente.setText(self.venda.cliente.nome)
        self.campData.setText(self.venda.data)
        self.campQtd.setText(str(self.venda.qtdItens()))
        self.campTotal.setText("R$ "+str(self.venda.getValorTotal()))

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)

        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(False)

    def carregaVendas(self):
        lista_de_itens = self.venda.lista_de_itens
        self.tableWidget.setRowCount(0)
        for info in lista_de_itens:
            self._addRow(info)

    def _addRow(self, item):
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        produto = QTableWidgetItem(item.getNomeProduto())
        valorunit = QTableWidgetItem(str(item.getValorUnitario()))
        valorunit.setTextAlignment(Qt.AlignCenter)
        qtd = QTableWidgetItem(str(item.quantidade))
        qtd.setTextAlignment(Qt.AlignCenter)
        valortot = QTableWidgetItem(str(item.getValor()))
        valortot.setTextAlignment(Qt.AlignCenter)
        
        self.tableWidget.setItem(rowCount, 0, produto)
        self.tableWidget.setItem(rowCount, 1, valorunit)
        self.tableWidget.setItem(rowCount, 2, qtd)
        self.tableWidget.setItem(rowCount, 3, valortot)

        