class Stock:
    def __init__(self):
        self.__amount = 0

    def set_amount(self, qtd):
        self.__amount += qtd

    def set_remove_amount(self, qtd):
        self.__amount -= qtd


    def consult(self):
        return f'Estoque atual: {self.__amount} unidades'


my_stock = Stock()
my_stock.set_amount(50)
my_stock.set_remove_amount(20)
print(my_stock.consult())
