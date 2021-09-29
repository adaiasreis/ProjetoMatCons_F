from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import uic
import sys
from ui.ui_mainWindow import MainWindow
import models.user_model as Usuarios

class FazerLogin(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/ui_telaLogin.ui",self)

        self.setEventos()

    def setEventos(self):
        self.b_entrar.clicked.connect(self.fazerLogin)
        self.b_sair.clicked.connect(self.Sair)
    
    def fazerLogin(self):

        while(True):

            self.l_info.setText("")
            usuario = ""
            senha = ""
            
            usuario = self.campUser.text()
            senha = self.campPassw.text()

            self.login = Usuarios.getLogin(usuario, senha)
            print(self.login)
            
            if  len(self.login) > 0:
                self.scre = MainWindow(self)
                self.scre.show()
                self.hide()
                self.limpaCampos()
                        
            else:
                self.l_info.setText("Dados de login incorretos. Tente novamente.")
                self.limpaCampos()
            break

    def Sair(self):
        self.close()

    def limpaCampos(self):
        self.newUser = None
        self.campUser.setText("")
        self.campPassw.setText("")

app = QApplication(sys.argv)
#apply_stylesheet(app, theme='dark_blue.xml')
window = FazerLogin()
window.show()
app.exec_()