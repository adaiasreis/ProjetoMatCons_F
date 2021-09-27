class User():
    def __init__ (self,id,nome,cpf,sexo,telefone,cargo,salario, ch_sem):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.telefone = telefone
        self.cargo = cargo
        self.salario = salario
        self.ch_sem = ch_sem

    def print(self):
        info = [self.id, self.nome, self.cpf, self.sexo,
                self.cargo, self.salario, self.ch_sem]
        print(info)
    
    def printInfo(self):
        info = [self.id, self.nome, self.telefone, self.cargo]
        print(info)