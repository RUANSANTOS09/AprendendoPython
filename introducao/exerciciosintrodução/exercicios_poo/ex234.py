class Product:
    def __init__(self,name, price):
        self.__name = name
        self.__price = price

    def get_price(self):
        return self.__price

    def get_name(self):
        return self.__name

    def info(self):
        return f'{self.get_name()} custa R$ {self.get_price()}'

class ImportedProduct(Product):
    def __init__(self,name,price,import_tax):
        self.__import_tax = import_tax
        super().__init__(name, price)

    def get_tax(self):
        return self.__import_tax

    def final_price(self):
        return self.get_price() + (self.get_price() * self.get_tax())

my_product_imported = ImportedProduct('Iphone', 4900.00, 0.15)
my_product = Product('Iphone', 4900.00)
print(f'{my_product.info()}\nCom a taxa de 15% passará a custar R$ {my_product_imported.final_price()}')
