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
                cursor.execute('INSERT INTO Item_Compra (Quantidade, Compra_ID, Produto_ID) VALUES ({}, {}, {})'.format(1, id_compra, i[0][0]))
                dao_bd.commit()            
            print("select com sucesso")
            dao_bd.encerra_bd(dao)
            return cursor.fetchall()           
        except:
            print("erro no select")
            dao_bd.rollback()
        
        dao.encerra_bd(dao_bd)
