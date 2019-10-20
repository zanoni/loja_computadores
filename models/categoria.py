class Categoria:
    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome():
        return self.__nome