class Compra:
    def ___init__(self):
        pass
    def calcula_total(self, produtos_selecionados):
        valor_total = 0
        for i in range(len(produtos_selecionados)):
            valor_total += produtos_selecionados[i][0][3]
        return valor_total