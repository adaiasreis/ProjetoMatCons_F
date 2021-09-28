from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem, QRadioButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt, QSize

class TableItens():
    def __init__(self, tableWidget, parent):
        self.tableWidget = tableWidget
        self.parent = parent
        
        self.itemAtual = None
        self.listaItens = []

        self.configTable()

        self.tableWidget.setRowCount(0)

    def configTable(self):
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setStretchLastSection(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.clicked.connect(self.on_click)

    def on_click(self):
        selected_row = self.tableWidget.currentRow()
        self.itemAtual = self.listaItens[selected_row]
        self.parent.b_removerItem.setEnabled(True)

    def _addRow(self, item):
        self.listaItens.append(item)
        rowCount = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowCount)
        qtd = QTableWidgetItem(str(item.quantidade))
        nome_produto = QTableWidgetItem(item.getNomeProduto())
        uni = QTableWidgetItem(str(item.getValorUni()))
        valor = QTableWidgetItem(str(item.getValor()))
        self.tableWidget.setItem(rowCount, 0, qtd)
        self.tableWidget.setItem(rowCount, 1, nome_produto)
        self.tableWidget.setItem(rowCount, 2, uni)
        self.tableWidget.setItem(rowCount, 3, valor)
        #self.tableWidget.setCellWidget(rowCount, 4, CustomQWidget(item, self))

        self.calculaValorTotal()

    def calculaValorTotal(self):
        valorTotal = 0
        desconto = self.parent.campDesconto.text()
        if desconto == "":
            desconto = "0"

        for item in self.listaItens:
            valorTotal += (float(item.getValor()))


        desconto = float(desconto)  # converte para float
        if desconto < valorTotal:
            valorTotal = valorTotal - desconto

        self.parent.campValorTotal.setText("%.2f" % valorTotal)

    def clickedCheck(self):
        if self.parent.r_din.setChecked(True):
            self.clickDin()
        elif self.parent.r_cred.setChecked(True):
            self.clickCred()
        elif self.parent.r_carCred.setChecked(True):
            self.click_cCred()
        elif self.parent.r_carDeb.setChecked(True):
            self.click_cDed()
    
    #Compra em DINHEIRO
    def clickDin(self):
        valorTotalP = 0.0
        desconto = 0.0
        valorTotal = self.parent.campValorTotal.text()
        if valorTotal == "":
            valorTotal = 0
        else:
            valorTotal = float(valorTotal)

        if desconto == "":
            desconto = 0
        
        radioBtn = self.parent.sender()
        if radioBtn.isChecked():
            desconto = valorTotal * 0.2
            valorTotalP = valorTotal - desconto

        self.parent.campDesconto.setText("%.2f" % desconto)
        self.parent.campTotalPagar.setText("%.2f" % valorTotalP)
            
    #Compra no CREDIARIO
    def clickCred(self):
        valorTotalP = 0.0
        desconto = 0.0
        valorTotal = self.parent.campValorTotal.text()
        if valorTotal == "":
            valorTotal = 0
        else:
            valorTotal = float(valorTotal)

        if desconto == "":
            desconto = 0

        radioBtn = self.parent.sender()
        if radioBtn.isChecked():
            desconto = valorTotal * 0.15
            valorTotalP = valorTotal + desconto
        self.parent.campDesconto.setText("0.0")
        self.parent.campTotalPagar.setText("%.2f" % valorTotalP)

    #Compra no CARTAO DE CREDITO
    def click_cCred(self):
        valorTotalP = 0.0
        desconto = 0.0
        valorTotal = self.parent.campValorTotal.text()
        if valorTotal == "":
            valorTotal = 0
        else:
            valorTotal = float(valorTotal)

        if desconto == "":
            desconto = 0

        radioBtn = self.parent.sender()
        if radioBtn.isChecked():
            desconto = valorTotal * 0.05
            valorTotalP = valorTotal - desconto
        self.parent.campDesconto.setText("%.2f" % desconto)
        self.parent.campTotalPagar.setText("%.2f" % valorTotalP)

    #Compra no CARTAO DE DEBITO
    def click_cDed(self):
        valorTotalP = 0.0
        desconto = 0.0
        valorTotal = self.parent.campValorTotal.text()
        if valorTotal == "":
            valorTotal = 0
        else:
            valorTotal = float(valorTotal)

        if desconto == "":
            desconto = 0

        radioBtn = self.parent.sender()
        if radioBtn.isChecked():
            desconto = valorTotal * 0.15
            valorTotalP = valorTotal - desconto
        self.parent.campDesconto.setText("%.2f" % desconto)
        self.parent.campTotalPagar.setText("%.2f" % valorTotalP)

    def limparItens(self):
        self.tableWidget.setRowCount(0)
        self.itemAtual = None
        self.listaItens = []
        #desativa os botões
        self.parent.b_removerItem.setEnabled(False)
        self.parent.b_limparItens.setEnabled(False)
        self.parent.carregaDadosProdutos()
        self.calculaValorTotal()

    def limparSelecionado(self):
        self.listaItens.remove(self.itemAtual)
        novaLista = self.listaItens

        self.limparItens()
        self.parent.b_limparItens.setEnabled(True)
        for prod in novaLista:
            self._addRow(prod)

    def remover(self):
        self.parent.itemAtual = self.item
        self.parent.limparSelecionado()
        print("Remover o item: ",self.item.produto.nome)