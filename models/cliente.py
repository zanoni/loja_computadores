from flask import Flask
from dao.cliente_dao import ClienteDao 
import json
class Cliente:
    def __init__(self):
        self.__nome = ''
        self.__email = ''
        self.__senha = ''

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def email(self):  #validar se tem o email cadastrado e não permitir cadastro repetido
        return self.__email
    @email.setter
    def email(self, email):
        self.__email = email
    
    @property
    def senha(self):
        return self.__senha
    @senha.setter
    def senha(self, senha):
        self.__senha = senha


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

    def autentica(self, cliente, senha):
        dao_cliente = ClienteDao()
        cliente = dao_cliente.select_por_email(cliente[0][2])       
        autentica = cliente[0][3] == senha       

        if autentica:
            cliente_logado = Cliente()
            cliente_logado.nome = cliente[0][1]
            cliente_logado.email = cliente[0][2]
            cliente_logado.senha = cliente[0][3]
            return cliente_logado.toJSON()
        
        return None

    def cadastra_cliente(self, cliente, nome, usuario, senha):        
        cliente.nome = nome
        cliente.email = usuario
        cliente.senha = senha
        return cliente
           
    
    