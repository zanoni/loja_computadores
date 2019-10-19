from flask import Flask, session
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
    
    def autentica(self, usuario, senha):
        autentica = self.__email == usuario and self.__senha == senha
        #fazer um select pra instanciar a classe cliente e para validar o usuario
        if autentica:

            session['logado'] = 
            

