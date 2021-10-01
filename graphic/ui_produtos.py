from utils.produtos import Produto
from PyQt5.QtWidgets import QWidget
from PyQt5 import uic
from table.data_tableProd import TableWidget

class CadProdutos(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_produtos.ui",self)
        self.table = TableWidget(self)
        self.verticalLayout.addWidget(self.table)

        # eventos dos botões
        self.setEventos()

        # mantém a referencia do contato selecionado atualmente para uma futura atualização ao salvar
        self.produtoAtual = None

    def setEventos(self):
        self.b_novo.clicked.connect(self.addProduto)
        self.b_limpar.clicked.connect(self.limpaCampos)
        self.b_excluir.clicked.connect(self.excluirItem)

    def addProduto(self):
        # adiciona os campos na tabela
        novoProduto = self.getProduto()
        # verifica os campos vazios
        if novoProduto != None:
            # é um novo contato
            if self.produtoAtual == None:
                # manda add no banco de dados
                self.table.add(novoProduto)
            else:
                # manda editar no bando de dados
                novoProduto.id = self.produtoAtual.id
                self.table.update(novoProduto)
            # limpa os campos
            self.limpaCampos()

    # pega as informações digitadas nos campos do Contato
    def getProduto(self):
        nome = self.campNome.text()
        marca = self.campMarca.text()
        descricao = self.campDescricao.text()
        preco_compra = self.campPreco_compra.text()
        preco_venda = self.campPreco_venda.text()
        quantidade = self.campQuantidade.text()

        if((nome != "") and (marca != "") and (descricao != "") and (preco_compra != "") and (preco_venda != "") and (quantidade != "")):
            return Produto(-1, self.campNome.text(), self.campMarca.text(), self.campDescricao.text(), self.campPreco_compra.text(), self.campPreco_venda.text(), self.campQuantidade.text())
        return None

    # limpa os campos e restaura os valores originais dos componentes
    def limpaCampos(self):
        self.produtoAtual = None
        self.campNome.setText("")
        self.campMarca.setText("")
        self.campDescricao.setText("")
        self.campPreco_compra.setText("")
        self.campPreco_venda.setText("")
        self.campQuantidade.setText("")

        self.b_novo.setText("Adicionar")
        self.b_excluir.setEnabled(False)

    # utilizado para preencher os campos na janela principal
    def insereProduto(self, produto):
        self.produtoAtual = produto
        self.campNome.setText(produto.nome)
        self.campMarca.setText(produto.marca)
        self.campDescricao.setText(produto.descricao)
        self.campPreco_compra.setText(str(produto.preco_compra))
        self.campPreco_venda.setText(str(produto.preco_venda))
        self.campQuantidade.setText(str(produto.quantidade))

        # muda o nome do botão para atualizar (já que existe o Contato)
        self.b_novo.setText("Atualizar")
        self.b_excluir.setEnabled(True)

    def excluirItem(self):
        self.table.delete(self.produtoAtual)
        # limpa os campos
        self.limpaCampos()