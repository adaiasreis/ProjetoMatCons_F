import sqlite3
from utils.clientes import Cliente

#pega todos os clientes do banco de dados
def getClientes():
    #cria a conexão
    conn = sqlite3.connect('models/db_matcons.db')
    #comunicação com o banco de dados
    cursor = conn.cursor()
    #executa o camando de seleção dos clientes
    cursor.execute("SELECT * FROM Clientes;")
    #imprime o resultado
    #CRIAR OS OBJETOS
    lista_clientes = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        cpf = l[2]
        telefone = l[3]
        email = l[4]
        endereco = l[5]
        novo = Cliente(id, nome, cpf, telefone, email, endereco)
        lista_clientes.append(novo)
    #fecha a conexão
    conn.close()
    return lista_clientes

def getCliente(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = """SELECT * FROM Clientes WHERE id = ?;"""
    cursor.execute(sql, [id])  
    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    cpf = l[2]
    telefone = l[3]
    email = l[4]
    endereco = l[5]
    novoCliente = Cliente(id, nome, cpf, telefone, email, endereco)
    conn.close()
    return novoCliente

def addCliente(cliente):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("INSERT INTO Clientes(nome, cpf, telefone, email, endereco) VALUES(?,?,?,?,?);")
    cursor.execute(sql, [cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco])
    #grava os dados no banco de dados
    conn.commit()
    conn.close()

def editCliente(cliente):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("UPDATE Clientes SET nome=?, telefone=?, email=?, endereco=? WHERE id=?;")
    print([cliente.nome, cliente.cpf, cliente.telefone, cliente.email, cliente.endereco])
    cursor.execute(sql, [cliente.nome, cliente.telefone, cliente.email, cliente.endereco, cliente.id])
    conn.commit()
    conn.close()

def delCliente(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("DELETE FROM Clientes WHERE id=?;")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()
    
    """try:
        num = int(input("Digite um número: "))
    except:
        print("Isso não é um número!")
    finally:
        print("Programa executado com sucesso!!!")"""