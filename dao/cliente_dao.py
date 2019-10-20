import MySQLdb
from flask import Flask
from dao.connect_bd import ConnectBd
class ClienteDao:

    
    def insert_cliente(self, cliente):
        dao = ConnectBd()
        dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
        cursor = dao_bd.cursor()

        cursor.execute('SELECT * FROM Cliente')
        try:
            if cliente.email not in cursor.fetchall():
                cursor.execute("INSERT INTO Cliente (Nome, Email, Senha) values('{}','{}','{}')".format(cliente.nome, cliente.email, cliente.senha))
                dao_bd.commit()
                print("insert com sucesso")
        except:
            print("erro no insert")
            dao_bd.rollback()

        dao.encerra_bd(dao_bd)
    
    def select_por_email(self, email):

        dao = ConnectBd()
        dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
        cursor = dao_bd.cursor()     
        try:
            cursor.execute('SELECT * FROM Cliente WHERE Email = "{}"'.format(email))
            cliente = cursor.fetchall()

            dao.encerra_bd(dao_bd)
            return cliente        
        except:
            dao.encerra_bd(dao_bd)
            return None
