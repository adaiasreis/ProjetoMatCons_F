from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.clientes_model as Clientes

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 4)
        self.parent = parent

        # textos do cabeçalho
        headers = ["ID", "NOME", "CPF","TELEFONE"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        # Carrega os dados do banco
        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        # ajusta as colunas ao tamanho da tela
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(0,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        # Alterna as cores das linhas
        self.setAlternatingRowColors(True)
        # desabilita a edição dos campos
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        # seleciona toda a linha
        self.setSelectionBehavior(QTableWidget.SelectRows)
        # evento ao selecionar uma linha
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_clientes = Clientes.getClientes()
        # necessário marcar a linha como a primeira para sobreescrever os dados da tabela
        self.setRowCount(0)
        for cliente in self.lista_clientes:
            self._addRow(cliente)

    def _addRow(self, cliente):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        # fixa a linha e muda a coluna conforme os valores
        id_item = QTableWidgetItem(str(cliente.id))
        id_nome = QTableWidgetItem(cliente.nome)
        id_cpf = QTableWidgetItem(cliente.cpf)
        id_telefone = QTableWidgetItem(cliente.telefone)

        # insere os itens na tabela
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_cpf)
        self.setItem(rowCount, 3, id_telefone)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        cliente = Clientes.getCliente(id)
        self.parent.insereCliente(cliente)

    # funções para adicionar no banco de dados
    def add(self, cliente):
        Clientes.addCliente(cliente)
        # Carrega os dados do banco
        self.carregaDados()

    def update(self, cliente):
        Clientes.editCliente(cliente)
        # Carrega os dados do banco
        self.carregaDados()

    def delete(self, cliente):
        Clientes.delCliente(cliente.id)
        # Carrega os dados do banco
        self.carregaDados()
