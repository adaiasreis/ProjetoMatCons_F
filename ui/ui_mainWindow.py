import sys
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import uic
from qt_material import apply_stylesheet

from ui.ui_produtos import CadProdutos
from ui.ui_clientes import CadClientes
from ui.ui_novaVenda import NovaVenda
from ui.ui_user import CadUser
from ui.ui_vendas import Vendas
#from ui.ui_venda

class MainWindow(QMainWindow):
    def __init__(self, janelaLogin):
        super().__init__()
        self.janelaLogin = janelaLogin
        uic.loadUi("ui/ui_mainWindow.ui",self)

        self.listWidget.insertItem(0, "PRODUTOS")
        self.listWidget.insertItem(1, "CLIENTES")
        self.listWidget.insertItem(2, "FUNCIONÁRIOS")
        self.listWidget.insertItem(3, "NOVA VENDA")
        self.listWidget.insertItem(4, "VENDAS")

        self.listWidget.setCurrentRow(0)

        self.carregaJanelas()
        
        self.listWidget.currentRowChanged.connect(self.display)


    def carregaJanelas(self):
        self.stackedWidget.insertWidget(0, CadProdutos())
        self.stackedWidget.insertWidget(1, CadClientes())
        self.stackedWidget.insertWidget(2, CadUser())
        self.stackedWidget.insertWidget(3, NovaVenda(self))
        self.stackedWidget.insertWidget(4, Vendas(self))

    def display(self, index):
        # necessário carregar as janelas a cada trasição para atualizar as informações
        self.carregaJanelas()
        self.stackedWidget.setCurrentIndex(index)

    def closeEvent(self, event):
        self.janelaLogin.show()