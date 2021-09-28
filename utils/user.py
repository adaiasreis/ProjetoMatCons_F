class User():
    def __init__ (self,id,nome,email,cpf,sexo,telefone,cargo,salario, ch_sem,user,passw):
        self.id = id
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.sexo = sexo
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario
        self.ch_sem = ch_sem
        self.user = user
        self.passw = passw

    def print(self):
        info = [self.id, self.nome, self.email, self.cpf, self.sexo,
                self.cargo, self.salario, self.ch_sem, self.user, self.passw]
        print(info)
    
    def printInfo(self):
        info = [self.id, self.nome, self.email, self.telefone, self.cargo]
        print(info)