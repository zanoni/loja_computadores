import MySQLdb
from flask import Flask
from dao.connect_bd import ConnectBd
class ProdutoDao:

    
    def select_produto_por_id(self, id_):
        dao = ConnectBd()
        dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
        cursor = dao_bd.cursor()

        try:           
            cursor.execute('SELECT * FROM Produto WHERE ID = {}'.format(id_))            
            produto = cursor.fetchall()
            print("select com sucesso")
            return produto
        except:
            print("erro no select")
            dao_bd.rollback()

        dao.encerra_bd(dao_bd)
    
    def select_produtos(self):
        dao = ConnectBd()
        dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
        cursor = dao_bd.cursor()
        produtos = []       

        try:
            cursor.execute('SELECT * FROM Produto')

            for i in cursor.fetchall():
                produtos.append(i)

            dao.encerra_bd(dao_bd)
            return produtos
           
        except:
            print("erro no insert")
            dao_bd.rollback()
            dao.encerra_bd(dao_bd)
        
    