from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QDateTime, QRegExp, QDate

import models.clientes_model as Clientes
import models.produtos_model as Produtos
import models.vendas_model as Vendas
from table.data_tableVenda import TableItens
from utils.item_venda import ItemVenda
from utils.venda import Venda
from ui.ui_fecharVenda import FecharVenda


class NovaVenda(QWidget):
    def __init__(self, parent):
        super(). __init__()
        self.parent = parent
        uic.loadUi("ui/ui_novaVenda.ui", self)

        self.clienteAtual = None
        self.produtoAtual = None
        self.lista_clientes = []
        self.lista_produtos = []

        self.setEventos()

        self.carregaDadosClientes()
        self.carregaDadosProdutos()

        # classe para o controle do QTableWidget
        self.tabelaItens = TableItens(self.tableWidget, self)

        # para valição do campo QUANTIDADE
        # só é permitido valores inteiros e número com 5 algarismos
        """mais exemplos: https://www.programcreek.com/python/example/106688/PyQt5.QtGui.QRegExpValidator"""
        qtd_validator = QRegExpValidator(QRegExp('^[1-9]{1}[0-9]{5}$'), self.campQuantidade)
        self.campQuantidade.setValidator(qtd_validator)

        desconto_validator = QRegExpValidator(QRegExp('^[0-9]+(\.[0-9]{1,2})?$'), self.campDesconto)
        self.campDesconto.setValidator(desconto_validator)

        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

    def carregaDadosClientes(self):
        # dados do cliente
        self.lista_clientes = Clientes.getClientes()
        lista_combo = []
        for cli in self.lista_clientes:
            lista_combo.append(cli.nome)
        self.combo_clientes.addItems(lista_combo)
    
    def carregaDadosProdutos(self):
        # dados do cliente
        self.lista_produtos = Produtos.getProdutos()
        lista_combo = []
        for prod in self.lista_produtos:
            lista_combo.append(prod.nome)
        self.combo_produtos.addItems(lista_combo)

    def setEventos(self):
        # Envia a posição atual do item
        self.combo_clientes.currentIndexChanged.connect(self.index_changed_cliente)
        self.combo_produtos.currentIndexChanged.connect(self.index_changed_produto)
        # botão add item
        self.b_addItem.clicked.connect(self.addItem)
        # botão limpar itens
        self.b_limparItens.clicked.connect(self.limparItens)
        # remove o item selecionado
        self.b_removerItem.clicked.connect(self.limparSelecionado)
        # verifica a quantidade digitada
        self.campQuantidade.textEdited.connect(self.qtd_edited)
        # prepara o fechamento da compra
        self.b_fecharVenda.clicked.connect(self.finalizaVenda)
        #As formas de pagamento
        self.r_din.toggled.connect(self.clikedDin)
        self.r_cred.toggled.connect(self.clickedCred)
        self.r_carDeb.toggled.connect(self.clikedCCred)
        self.r_carCred.toggled.connect(self.clikedCDeb)

    def atualizaValorTotal(self):
        self.tabelaItens.calculaValorTotal()

    # CLIENTE
    def index_changed_cliente(self, i):  # i é a posição do item selecionado
        # a lista do comboBox e a lista de clientes possuem o mesmo tamanho e itens, logo são iguais e podemos pegar o mesmo item da lista, o objeto cliente desejado
        self.clienteAtual = self.lista_clientes[i]
        # coloca i ID no campo de visualização
        self.id_lineEdit.setText(str(self.lista_clientes[i].id))
    
    # PRODUTO
    def index_changed_produto(self, i):  # i é a posição do item selecionado
        self.produtoAtual = self.lista_produtos[i]
        self.campMarca.setText(self.lista_produtos[i].marca)
        self.campValor.setText(str(self.lista_produtos[i].preco_venda))
        self.campQtd_disp.setText(str(self.lista_produtos[i].quantidade))
        self.campDesc.setText(self.lista_produtos[i].descricao)

    
    # adiciona um item na tabela
    def addItem(self):
        item = ItemVenda(self.campQuantidade.text(), self.produtoAtual, self.campValor)
        self.tabelaItens._addRow(item)
        self.b_limparItens.setEnabled(True)
        self.b_fecharVenda.setEnabled(True)
        self.b_addItem.setEnabled(False)
        self.campQuantidade.setText("")

        # REDUZ TEMPORARIAMENTE A QUANTIDADE DO ITEM NA LISTA DE PRODUTOS
        index = self.lista_produtos.index(self.produtoAtual)
        p = self.lista_produtos[index]
        p.quantidade = item.novaQtd()

        # ATUALIZA A LISTA DE PRODUTOS
        self.atualizaListaProdutos()

    def atualizaListaProdutos(self):
        self.combo_produtos.clear()
        lista_combo = []
        for c in self.lista_produtos:
            lista_combo.append(c.nome)
        self.combo_produtos.addItems(lista_combo)

    #limpa os itens da tabela
    def limparItens(self):
        self.tabelaItens.limparItens()

    #limpa um item da tabela
    def limparSelecionado(self):
        self.tabelaItens.limparSelecionado()

    #executa a função toda vez que quantidade for digitado
    def qtd_edited(self, quan):
        #habilita o botão de adicionar apenas se tiver a quantidade disponível
        if quan != "" and int(quan) <= self.produtoAtual.quantidade:
            self.b_addItem.setEnabled(True)
        else:
            self.b_addItem.setEnabled(False)

    def clikedDin(self):
        self.tabelaItens.clickDin()

    def clickedCred(self):
        self.tabelaItens.clickCred()

    def clikedCCred(self):
        self.tabelaItens.click_cCred()

    def clikedCDeb(self):
        self.tabelaItens.click_cDed()

    def finalizaVenda(self):
        #pega a data em string
        data = self.dateTimeEdit.dateTime().toString('dd/MM/yyyy')
        cliente = self.clienteAtual
        lista_de_itens = self.tabelaItens.listaItens
        valor_total = self.campValorTotal.text()
        novaVenda = Venda(-1, cliente, lista_de_itens, valor_total, data)
        Vendas.addVenda(novaVenda)
        self.limparItens()

        #self.fecharVenda(novaVenda)

    def fecharVenda(self, winVenda):
        self.finalC = FecharVenda(winVenda)
        self.finalC.show()
        self.limparItens()
