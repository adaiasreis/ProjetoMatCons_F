import sqlite3
from utils.user import User

def getUsuarios():
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Usuarios;")
    lista_user = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        cpf = l[2]
        sexo = l[3]
        telefone = l[4]
        cargo = l[5] 
        salario = l[6]
        ch_sem = l[7]
        novoUser = User(id, nome, cpf, sexo, telefone, cargo, salario, ch_sem)
        lista_user.append(novoUser)
    conn.close()
    return lista_user

def getUsuario(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = """SELECT * FROM Usuarios WHERE ID = ?;"""
    cursor.execute(sql, [id])
    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    cpf = l[2]
    sexo = l[3]
    telefone = l[4]
    cargo = l[5]
    salario = l[6]
    ch_sem = l[7]
    novoUser = User(id, nome, cpf, sexo, telefone, cargo, salario, ch_sem)
    conn.close
    return novoUser

def addUsuario(user):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("INSERT INTO Usuarios (nome, cpf, sexo, telefone, cargo, salario, ch_sem) VALUES (?, ?, ?, ?, ?, ?, ?);")
    cursor.execute(sql,[user.nome,user.cpf, user.sexo, user.telefone, user.cargo, user.salario, user.ch_sem])
    conn.commit()
    conn.close()
    print("\n\nUsuário adicionado com sucesso!")

def editUsuario(user):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("UPDATE Usuarios SET nome = ?, cpf = ?, sexo = ?, telefone = ?, cargo = ?, salario = ?, ch_sem = ? WHERE id = ?")
    print([user.nome, user.cpf, user.sexo, user.telefone, user.cargo, user.salario, user.ch_sem])
    cursor.execute(sql,[user.nome, user.cpf, user.sexo, user.telefone, user.cargo, user.salario, user.ch_sem, user.id])
    conn.commit()
    conn.close()

def delUsuario(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = (" DELETE FROM Usuarios WHERE id = ?")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()