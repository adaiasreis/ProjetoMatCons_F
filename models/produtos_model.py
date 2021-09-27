import sqlite3
from utils.produtos import Produto

def getProdutos():
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Produtos;")
    lista_produtos = []
    for l in cursor.fetchall():
        id = l[0]
        nome = l[1]
        marca = l[2]
        descricao = l[3] 
        preco_compra = l[4]
        preco_venda = l[5]
        quantidade = l[6]
        novoProduto = Produto(id, nome, marca, descricao, preco_compra, preco_venda, quantidade)
        lista_produtos.append(novoProduto)
    conn.close()
    return lista_produtos

def getProduto(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = """SELECT * FROM Produtos WHERE ID = ?;"""
    cursor.execute(sql, [id])
    l = cursor.fetchall()[0]
    id = l[0]
    nome = l[1]
    marca = l[2]
    descricao = l[3] 
    precocompra = l[4]
    precovenda = l[5]
    quantidade = l[6]
    novoProduto = Produto(id, nome, marca, descricao, precocompra, precovenda, quantidade)
    conn.close
    return novoProduto

def addProduto(produto):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("INSERT INTO Produtos (nome, marca, descricao, preco_compra, preco_venda, quantidade) VALUES (?, ?, ?, ?, ?, ?);")
    cursor.execute(sql,[produto.nome, produto.marca, produto.descricao, produto.preco_compra, produto.preco_venda, produto.quantidade])
    conn.commit()
    conn.close()
    print("\n\nCliente adicionado com sucesso!")

def editProduto(produto):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = ("UPDATE Produtos SET nome = ?, marca = ?, descricao = ?, preco_compra = ?, preco_venda = ?, quantidade = ? WHERE id = ?")
    print([produto.nome, produto.marca, produto.descricao, produto.preco_compra, produto.preco_venda, produto.quantidade])
    cursor.execute(sql,[produto.nome, produto.marca, produto.descricao, produto.preco_compra, produto.preco_venda, produto.quantidade, produto.id])
    conn.commit()
    conn.close()

def delProduto(id):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    sql = (" DELETE FROM Produtos WHERE id = ?")
    cursor.execute(sql, [id])
    conn.commit()
    conn.close()