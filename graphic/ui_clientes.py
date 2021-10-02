from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from table.data_tableCli import TableWidget
from utils.clientes import Cliente
from graphic.ui_historicoCliente import HistoricoCliente
import models.vendas_model as Vendas

class CadClientes(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_clientes.ui",self)
        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        # eventos dos botões
        self.setEventos()

        # mantém a referencia do contato selecionado atualmente para uma futura atualização ao salvar
        self.clienteAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addCliente)
        self.b_limpar.clicked.connect(self.limpaCampos)
        self.b_excluir.clicked.connect(self.excluirItem)
        self.b_historico.clicked.connect(self.historicoCliente)

    def addCliente(self):
        # adiciona os campos na tabela
        novoCliente = self.getClientes()
        # verifica os campos vazios
        if novoCliente != None:
            # é um novo contato
            if self.clienteAtual == None:
                # manda add no banco de dados
                self.table.add(novoCliente)
            else:
                # manda editar no bando de dados
                novoCliente.id = self.clienteAtual.id
                self.table.update(novoCliente)
            # limpa os campos
            self.limpaCampos()

    # pega as informações digitadas nos campos do Contato
    def getClientes(self):
        nome = self.campNome.text()
        cpf = self.campCpf.text()
        telefone = self.campTelefone.text()
        email = self.campEmail.text()
        endereco = self.campEndereco.text()

        if((nome != "") and (cpf != "") and (telefone != "") and (email != "") and (endereco != "")):
            return Cliente(-1, self.campNome.text(), self.campCpf.text(), self.campTelefone.text(), self.campEmail.text(), self.campEndereco.text())
        return None

    # limpa os campos e restaura os valores originais dos componentes
    def limpaCampos(self):
        self.clienteAtual = None
        self.campNome.setText("")
        self.campCpf.setText("")
        self.campTelefone.setText("")
        self.campEmail.setText("")
        self.campEndereco.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)
        self.b_historico.setEnabled(False)

    # utilizado para preencher os campos na janela principal
    def insereCliente(self, cliente):
        self.clienteAtual = cliente
        self.campNome.setText(cliente.nome)
        self.campCpf.setText(cliente.cpf)
        self.campTelefone.setText(cliente.telefone)
        self.campEmail.setText(cliente.email)
        self.campEndereco.setText(cliente.endereco)

        # muda o nome do botão para atualizar (já que existe o Contato)
        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)
        self.b_historico.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.clienteAtual)
        # limpa os campos
        self.limpaCampos()

    def historicoCliente(self):
        self.historico = HistoricoCliente(self.clienteAtual)
        self.historico.show()