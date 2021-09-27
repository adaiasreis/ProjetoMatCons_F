from PyQt5.QtWidgets import QHeaderView, QTableWidget, QTableWidgetItem

import models.user_model as Usuarios

class TableWidget(QTableWidget):
    def __init__(self, parent):
        super().__init__(0, 4)
        self.parent = parent

        headers = ["ID", "NOME","TELEFONE","CARGO"]
        self.setHorizontalHeaderLabels(headers)

        self.configTable()

        self.carregaDados()

    def configTable(self):
        self.verticalHeader().setVisible(False)
        self.horizontalHeader().setStretchLastSection(False)
        self.horizontalHeader().setSectionResizeMode(1,QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QHeaderView.ResizeToContents)
        self.horizontalHeader().setSectionResizeMode(3,QHeaderView.ResizeToContents)
        self.setEditTriggers(QTableWidget.NoEditTriggers)
        self.setSelectionBehavior(QTableWidget.SelectRows)
        self.clicked.connect(self.on_click)

    def carregaDados(self):
        self.lista_usuarios = Usuarios.getUsuarios()
        self.setRowCount(0)
        for user in self.lista_usuarios:
            self._addRow(user)

    def _addRow(self, user):
        rowCount = self.rowCount()
        self.insertRow(rowCount)
        id_item = QTableWidgetItem(str(user.id))
        id_nome = QTableWidgetItem(user.nome)
        id_telefone = QTableWidgetItem(user.telefone)
        id_cargo = QTableWidgetItem(user.cargo)
        
        self.setItem(rowCount, 0, id_item)
        self.setItem(rowCount, 1, id_nome)
        self.setItem(rowCount, 2, id_telefone)
        self.setItem(rowCount, 3, id_cargo)

    def on_click(self):
        selected_row = self.currentRow()
        id = self.item(selected_row, 0).text()
        user = Usuarios.getUsuario(id)
        self.parent.insereUser(user)

    def add(self, user):
        Usuarios.addUsuario(user)
        self.carregaDados()

    def update(self, user):
        Usuarios.editUsuario(user)
        self.carregaDados()

    def delete(self, user):
        Usuarios.delUsuario(user.id)

        self.carregaDados()