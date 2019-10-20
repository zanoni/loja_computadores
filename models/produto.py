class Produto:
    def __init__(self):
        self.__nome = ''
        self.__categoria_id = 0
        self.__preco = 0.00
        self.__img = ''            

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def categoria_id(self):
        return self.__categoria_id
    @categoria_id.setter
    def categoria_id(self, categoria_id):
        self.__categoria_id = categoria_id

    @property
    def preco(self):
        return self.__preco
    @preco.setter
    def preco(self, preco):
        self.__preco = preco

    @property
    def img(self):
        return self.__img
    @img.setter
    def img(self, img):
        self.__img = img