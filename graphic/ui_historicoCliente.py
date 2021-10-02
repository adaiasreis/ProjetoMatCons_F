from PyQt5.QtWidgets import QWidget, QHeaderView, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import uic

import models.vendas_model as Vendas


class HistoricoCliente(QWidget):
    def __init__(self, cliente):
        super().__init__()
        uic.loadUi("ui/ui_historicoCliente.ui", self)

        self.cliente = cliente
        print(cliente.id)

        # Configuração da tabela
        self.configTable()
        self.insertDados()
        self.campNome.setText(self.cliente.nome)
        self.campTelefone.setText(self.cliente.telefone)

    def insertDados(self):
        lista_vendas = Vendas.getVendasCliente(self.cliente.id)
        print(lista_vendas)
        self.tableWidget.setRowCount(0)
        for v in lista_vendas:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            # insere os itens na tabela
            id = QTableWidgetItem(str(v.id))
            id.setTextAlignment(Qt.AlignCenter)
            data =  QTableWidgetItem(v.data)
            data.setTextAlignment(Qt.AlignCenter)
            qtd = QTableWidgetItem(str(v.qtdItens()))
            qtd.setTextAlignment(Qt.AlignCenter)
            vt = QTableWidgetItem(str(v.valor_total))
            vt.setTextAlignment(Qt.AlignCenter)
            self.tableWidget.setItem(rowCount, 0, id)
            self.tableWidget.setItem(rowCount, 1,data)
            self.tableWidget.setItem(rowCount, 2, qtd)
            self.tableWidget.setItem(rowCount, 3, vt)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
         # Alterna as cores das linhas
        self.tableWidget.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)