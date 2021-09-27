from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.produtos_model as Produtos

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 6)
        self.parent = parent

        # textos do cabeçalho
        headers = ["ID", "NOME", "MARCA", "PREÇO I R$", "PREÇO F R$", "QUANTIDADE"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        # Carrega os dados do banco
        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_produtos = Produtos.getProdutos()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for produto in self.lista_produtos:
            self._addRow(produto)

    def _addRow(self, produto):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(produto.id))
        id_nome = QTableWidgetItem(produto.nome)
        id_marca = QTableWidgetItem(produto.marca)
        id_preco_compra = QTableWidgetItem(str(produto.preco_compra))
        id_preco_venda = QTableWidgetItem(str(produto.preco_venda))
        id_quantidade = QTableWidgetItem(str(produto.quantidade))
        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_marca)
        self.setItem(rowCount, 3, id_preco_compra)
        self.setItem(rowCount, 4, id_preco_venda)
        self.setItem(rowCount, 5, id_quantidade)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        produto = Produtos.getProduto(id)
        self.parent.insereProduto(produto)

    # funções para adicionar no banco de dados
    def add(self, produto):
        Produtos.addProduto(produto)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, produto):
        Produtos.editProduto(produto)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, produto):
        Produtos.delProduto(produto.id)
        # Carrega os dados do banco
        self.carregaDados()