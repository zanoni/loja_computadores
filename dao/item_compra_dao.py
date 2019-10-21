import MySQLdb
from flask import Flask
from dao.connect_bd import ConnectBd
class ItemCompraDao:
    def salva_produtos_compra(self, produtos_bd, id_compra):
        dao = ConnectBd()
        dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
        cursor = dao_bd.cursor()

        try:     
            for i in produtos_bd:      
                cursor.execute('INSERT INTO Item_Compra (Quantidade, Compra_ID, Produto_ID) VALUES (1, {}, {})'.format(id_compra[0][0], i[0][0]))
                dao_bd.commit()            
            print("insert item_produto com sucesso")
            dao.encerra_bd(dao_bd)
            return cursor.fetchall()           
        except:
            print("erro insert item_produto")
            dao_bd.rollback()
        
        dao.encerra_bd(dao_bd)
