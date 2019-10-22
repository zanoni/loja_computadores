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

    # def update_cliente(self):

    #     dao = ConnectBd()
    #     dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
    #     cursor = dao_bd.cursor()
    #     try:
    #         cursor.execute("UPDATE Cliente SET nome='{}', cpf='{}', data_nascimento='{}' WHERE ID={}"
    #         .format(cliente.nome, cliente.cpf, cliente.nascimento , cliente.id))
    #         dao_bd.commit()
    #         dao.encerra_bd(dao_bd)
    #     except:
    #         dao.encerra_bd(dao_bd)
    #         return None


    # def delete_cliente(self, id_):
    #     dao = ConnectBd()
    #     dao_bd = dao.inicia_conexao('mysql.zuplae.com', 'zuplae11', 'grupo06', 'zuplae11')
    #     cursor = dao_bd.cursor()
    #     try:
    #         cursor.execute("DELETE FROM Cliente WHERE id={}".format(id_))
    #         dao_bd.commit()
    #         dao.encerra_bd(dao_bd)
    #     except:
    #         dao.encerra_bd(dao_bd)
    #         return None