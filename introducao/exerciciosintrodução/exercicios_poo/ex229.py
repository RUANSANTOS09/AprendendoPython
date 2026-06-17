class Cart:
    def __init__(self):
        self.__items = []

    def set_itens(self, itens):
        self.__items.append(itens)

    def get_total_items(self):
        return len(self.__items)

my_items = Cart()
my_items.set_itens('Item: Mouse ')
my_items.set_itens('Item: PC ')
my_items.set_itens('Item: Tv ')
my_items.set_itens('Item: Phone')
print(my_items.get_total_items())
