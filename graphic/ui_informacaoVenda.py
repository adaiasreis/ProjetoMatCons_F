from PyQt5.QtWidgets import QLabel, QVBoxLayout, QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton

from PyQt5 import uic
from PyQt5.QtCore import Qt

import models.vendas_model as Venda


class InfoVenda(QWidget):
    def __init__(self, venda):
        super().__init__()
        uic.loadUi("ui/ui_informacaoVenda.ui", self)

        self.venda = venda
        self.configTable()
        self.carregaVenda()

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

    def carregaVenda(self):
        lista_de_itens = []
        lista_de_itens = self.venda.lista_de_itens
        print(lista_de_itens)
        self.tableWidget.setRowCount(0)
        for i in lista_de_itens:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            produto = QTableWidgetItem(i.getNomeProduto())
            valorUni = QTableWidgetItem(str(i.getValorUni()))
            valorUni.setTextAlignment(Qt.AlignCenter)
            quantidade = QTableWidgetItem(str(i.quantidade))
            quantidade.setTextAlignment(Qt.AlignCenter)
            valorTotal = QTableWidgetItem(str(i.getValor()))
            valorTotal.setTextAlignment(Qt.AlignCenter)
            
            self.tableWidget.setItem(rowCount, 0, produto)
            self.tableWidget.setItem(rowCount, 1, valorUni)
            self.tableWidget.setItem(rowCount, 2, quantidade)
            self.tableWidget.setItem(rowCount, 3, valorTotal)

        