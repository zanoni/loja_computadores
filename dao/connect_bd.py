import MySQLdb
from flask import Flask

class ConnectBd:
    def inicia_conexao(self, host, database, passwd, user):
        return MySQLdb.connect(host=f'{host}', database=f'{database}',  user=f'{user}', passwd=f'{passwd}')
        
    def encerra_bd(self, sql):
        sql.close()