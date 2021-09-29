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
        email = l[2]
        cpf = l[3]
        sexo = l[4]
        telefone = l[5]
        cargo = l[6] 
        salario = l[7]
        ch_sem = l[8]
        user = [9]
        passw = [10]
        novoUser = User(id, nome, email, cpf, sexo, telefone, cargo, salario, ch_sem, user, passw)
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
    email = l[2]
    cpf = l[3]
    sexo = l[4]
    telefone = l[5]
    cargo = l[6]
    salario = l[7]
    ch_sem = l[8]
    user = l[9]
    passw = l[10]
    novoUser = User(id, nome, email, cpf, sexo, telefone, cargo, salario, ch_sem, user, passw)
    conn.close
    return novoUser

def addUsuario(user):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("INSERT INTO Usuarios (nome, email, cpf, sexo, telefone, cargo, salario, ch_sem, user, passw) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);")
    cursor.execute(sql,[user.nome,user.email,user.cpf,user.sexo,user.telefone,user.cargo,user.salario,user.ch_sem,user.user,user.passw])
    conn.commit()
    conn.close()
    print("\n\nUsuário adicionado com sucesso!")

def editUsuario(user):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("UPDATE Usuarios SET nome = ?, email = ?, cpf = ?, sexo = ?, telefone = ?, cargo = ?, salario = ?, ch_sem = ?, user = ?, passw = ? WHERE id = ?")
    print([user.nome, user.email, user.cpf, user.sexo, user.telefone, user.cargo, user.salario, user.ch_sem, user.user, user.passw])
    cursor.execute(sql,[user.nome, user.email, user.cpf, user.sexo, user.telefone, user.cargo, user.salario, user.ch_sem, user.user, user.passw, user.id])
    conn.commit()
    conn.close()

def delUsuario(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = (" DELETE FROM Usuarios WHERE id = ?")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()

def getLogin(user, passw):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("SELECT nome, user, passw FROM Usuarios WHERE user = ? AND passw = ?;")
    cursor.execute(sql, [user, passw])
    new_list = []
    for l in cursor.fetchall():
        user = l[0]
        passw = l[1]
        new = (user, passw)
        new_list.append(new)
    conn.close()
    return new_list