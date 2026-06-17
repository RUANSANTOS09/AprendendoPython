class SourceOfData:
    def __init__(self, name, type):
        self.__name = name
        self.__type = type
    def get_description(self):
        print(f'Fonte de Dados: {self.__name}, Tipo: {self.__type}')

my_source = SourceOfData('PostgreSQL Vendas', 'API')
my_source.get_description()
