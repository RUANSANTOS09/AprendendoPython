class File:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__lines = []

    def set_add_line(self,lines):
        self.__lines.append(lines)

    def get_total_lines(self):
       return len(self.__lines)

my_file = File('vendas.csv')
my_file.set_add_line('linha 1: venda de notebook')
my_file.set_add_line('linha 2: venda de mouse')
my_file.set_add_line('linha 3: venda de teclado')
print(my_file.get_total_lines())