import MySQLdb
from flask import Flask
from dao.connect_bd import ConnectBd
class CompraDao:

    def insert_compra(self, valor_total, cliente_id):
        dao = ConnectBd()
        dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
        cursor = dao_bd.cursor()

        try:           
            cursor.execute('INSERT INTO Compra (Valor_TOTAL, Cliente_ID) VALUES ({}, {})'.format(valor_total, cliente_id))
            dao_bd.commit()
            cursor.execute('SELECT * FROM Compra WHERE Cliente_ID = {} ORDER BY ID DESC LIMIT 1'.format(cliente_id))
            print("select com sucesso")
            dao.encerra_bd(dao)
            return cursor.fetchall()           
        except:
            print("erro no select")
            dao_bd.rollback()
        
        dao_bd.encerra_bd(dao)
    
        