from utils.item_venda import ItemVenda
from utils.venda import Venda
import sqlite3

import models.produtos_model as Produtos
import models.clientes_model as Clientes

def addVenda(venda):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()

    sql_addVenda = "INSERT INTO Vendas (id_cliente, valor_total, data) VALUES(?, ?, ?);"
    valuesVenda = [venda.cliente.id, venda.getValorTotal(), venda.data]
    cursor.execute(sql_addVenda, valuesVenda)
    conn.commit()

    sql_id_venda = "SELECT LAST_INSERT_ROWID() AS id;"
    cursor .execute(sql_id_venda)
    rowID = cursor.fetchall()[0]
    id_venda = rowID[0]

    sql_addItens = "INSERT INTO ItensVenda (id_venda, id_produto, quantidade, valor_unitario) VALUES (?, ?, ?, ?)"

    listaItens = venda.getItens()
    for item in listaItens:
        valuesItem = [id_venda, item.produto.id, item.quantidade, item.getValorUni()]
        cursor.execute(sql_addItens, valuesItem)
        conn.commit()

    conn.close

def getVendasCliente(id_cliente):
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    lista_de_vendas = []
    sql = "SELECT * FROM Vendas WHERE id_cliente = ?;" # ORDER BY data ASC
    cursor.execute(sql, [id_cliente])
    for v in cursor.fetchall():
        id_venda = v[0]
        id_cliente = v[1]
        valorTotal = v[2]
        data = v[3]
        lista_de_itens = []
        sql_itens = "SELECT * FROM ItensVenda WHERE id_venda = ?;"
        valuesItens = [id_venda]
        cursor.execute(sql_itens, valuesItens)
        for i in cursor.fetchall():
            id_produto = i[1]
            quantidade = i[2]
            valorUnitario = i[3]

            produto = Produtos.getProduto(id_produto)
            item = ItemVenda(quantidade, produto, valorUnitario)
            lista_de_itens.append(item)

        cliente = Clientes.getCliente(id_cliente)
        venda = Venda(id_venda, cliente, lista_de_itens, valorTotal, data)
        lista_de_vendas.append(venda)
    conn.close()
    return lista_de_vendas

def getVendas():
    conn = sqlite3.connect('models/db_matcons.db')
    cursor = conn.cursor()
    lista_de_vendas = []
    sql = "SELECT * FROM Vendas ORDER BY data desc;"
    cursor.execute(sql)
    for v in cursor.fetchall():
        id_venda = v[0]
        id_cliente = v[1]
        valorTotal = v[2]
        data = v[3]
        lista_de_itens = []
        sql_itens = "SELECT * FROM ItensVenda WHERE id_venda = ?;"
        valuesItens = [id_venda]
        cursor.execute(sql_itens, valuesItens)
        for i in cursor.fetchall():
            id_produto = i[1]
            quantidade = i[2]
            valorUnitario = i[3]

            produto = Produtos.getProduto(id_produto)
            item = ItemVenda(quantidade, produto, valorUnitario)
            lista_de_itens.append(item)

        cliente = Clientes.getCliente(id_cliente)
        venda = Venda(id_venda, cliente, lista_de_itens, valorTotal, data)
        lista_de_vendas.append(venda)
    conn.close()
    return lista_de_vendas