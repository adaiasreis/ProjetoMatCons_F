from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5.QtGui import QIcon
from PyQt5 import uic

import models.vendas_model as Venda
from graphic.ui_informacaoVenda import InfoVenda

"""#from layouts.ui_info_vendas import InfoVenda

TYPE = {'remove': 0, 'info': 1}"""


class Vendas(QWidget):
    def __init__(self, venda):
        super(). __init__()
        uic.loadUi("ui/ui_vendas.ui", self)

        self.venda = venda

        self.configTable()

        self.lista_de_vendas = []
        self.carregaVendas()

        self.b_novaVenda.clicked.connect(self.novaVenda)
        self.b_informacoes.clicked.connect(self.informacaoVenda)

    def novaVenda(self):
        self.parent.display(4)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        # ajusta a altura das linhas
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        # ajusta as colunas ao tamanho da tela
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.tableWidget.setSelectionBehavior(True)

    def carregaVendas(self):
        self.lista_de_vendas = Venda.getVendas()
        self.tableWidget.setRowCount(0)
        for v in self.lista_de_vendas:
            rowCount = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowCount)
            # fixa a linha e muda a coluna conforme os valores
            id = QTableWidgetItem(str(v.id))
            id.setTextAlignment(Qt.AlignCenter)
            data = QTableWidgetItem(v.data)
            data.setTextAlignment(Qt.AlignCenter)
            nome = QTableWidgetItem(v.cliente.nome)
            fone = QTableWidgetItem(v.cliente.telefone)
            fone.setTextAlignment(Qt.AlignCenter)
            valor = QTableWidgetItem(str(v.getValorTotal()))
            valor.setTextAlignment(Qt.AlignCenter)

            # insere os itens na tabela
            #self.tableWidget.setCellWidget(rowCount, 0, CustomQWidget(item, self, TYPE['info']))
            self.tableWidget.setItem(rowCount, 0, id)
            self.tableWidget.setItem(rowCount, 1, data)
            self.tableWidget.setItem(rowCount, 2, nome)
            self.tableWidget.setItem(rowCount, 3, fone)
            self.tableWidget.setItem(rowCount, 4, valor)
            #self.tableWidget.setCellWidget(rowCount, 6, CustomQWidget(item, self))
            self.b_informacoes.setEnabled(True)

    def informacaoVenda(self, venda):
        self.w = InfoVenda(self.carregaVendas())
        self.w.show()

"""class CustomQWidget(QWidget):
    def __init__(self, venda, parent, type):
        super(CustomQWidget, self).__init__()
        self.venda = venda
        self.parent = parent

        self.w = None

        self.btn = QPushButton(self)
        self.btn.setText("")  # text

        if type == TYPE['remove']:
            self.typeDelete()
        else:
            self.typeInfo()

        # remove a cor de fundo do botão e a borda
        self.btn.setStyleSheet(
            'QPushButton {background-color: #00FFFFFF; border:  none}')

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def typeInfo(self):
        self.btn.setIcon(QIcon("icons/info.png"))  # icon
        self.btn.clicked.connect(self.maisInfo)
        self.btn.setToolTip(
            "Mais informações sobre a venda.")  # Tool tip
        self.btn.setIconSize(QSize(25, 25))

    def typeDelete(self):
        self.btn.setIcon(QIcon("icons/delete.png"))  # icon
        self.btn.clicked.connect(self.remover)
        self.btn.setToolTip(
            "Remover venda?")  # Tool tip
        self.btn.setIconSize(QSize(20, 20))

    def remover(self):

        pass

    def maisInfo(self):
        self.w = InfoVenda(self.venda)
        self.w.show()"""