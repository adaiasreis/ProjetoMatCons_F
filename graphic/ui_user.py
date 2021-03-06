from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from table.data_tableUser import TableWidget
from utils.user import User

class CadUser(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_user.ui",self)
        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        self.userAtual = None

        self.index_changed_sexo()

        self.setEventos()

    def setEventos(self):
        self.b_novo.clicked.connect(self.addUsuario)
        self.b_limpar.clicked.connect(self.limpaCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def index_changed_sexo(self):
        self.comboSexos.addItems(["Masculino", "Feminino"])
        
    def addUsuario(self):
        novoUser = self.getUser()
        if novoUser != None:
            if self.userAtual == None:
                self.table.add(novoUser)
            else:
                novoUser.id = self.userAtual.id
                self.table.update(novoUser)
            self.limpaCampos()

    def getUser(self):
        nome = self.campNome.text()
        email = self.campEmail.text()
        cpf = self.campCpf.text()
        sexo = self.comboSexos.currentText()
        telefone = self.campTelefone.text()
        cargo = self.campCargo.text()
        salario = self.campSalario.text()
        ch_sem = self.campCh_sem.text()
        user = self.campUsuario.text()
        passw = self.campSenha.text()
        
        if ((nome != "") and (email != "") and (cpf != "")and (sexo != "") and (telefone != "") and (cargo != "") and (salario != "") and (ch_sem != "") and (user != "") and (passw != "")):
            return User(-1, self.campNome.text(), self.campCpf.text(), self.comboSexos.currentText(), self.campTelefone.text(), self.campCargo.text(), self.campSalario.text(), self.campCh_sem.text(), self.campUsuario.text(), self.campSenha.text())
        return None
    
    def limpaCampos(self):
        self.userAtual = None
        self.campNome.setText("")
        self.campEmail.setText("")
        self.campCpf.setText("")
        self.comboSexos.setCurrentText(None)
        self.campTelefone.setText("")
        self.campCargo.setText("")
        self.campSalario.setText("")
        self.campCh_sem.setText("")
        self.campUsuario.setText("")
        self.campSenha.setText("")
        
        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.campUsuario.setEnabled(True)
        self.campSenha.setEnabled(True)

    def insereUser(self, user):
        self.userAtual = user
        self.campNome.setText(user.nome)
        self.campEmail.setText(user.email)
        self.campCpf.setText(user.cpf)
        self.comboSexos.setCurrentText(user.sexo)
        self.campTelefone.setText(user.telefone)
        self.campCargo.setText(user.cargo)
        self.campSalario.setText(str(user.salario))
        self.campCh_sem.setText(str(user.ch_sem))
        
        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.campUsuario.setEnabled(False)
        self.campSenha.setEnabled(False)

    def excluirItem(self):
        self.table.delete(self.userAtual)
        self.limpaCampos()