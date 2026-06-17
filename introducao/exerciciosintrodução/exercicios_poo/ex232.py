class Employee:
    def __init__(self,name,wage):
        self.__name = name
        self.__wage = wage

    def get_name(self):
        return self.__name

    def get_wage(self):
        return self.__wage

    def get_description(self):
        print(f'{self.__name} ganha R$ {self.__wage}')

class Engineer(Employee):
    def __init__(self, name, wage, language):
        self.__language = language
        super().__init__(name,wage)

    def get_description(self):
        print(f'{self.get_name()} ganha R$ {self.get_wage()} e programa em {self.__language}')

my_engineer = Engineer('Ruan', 4900, 'Python')
my_engineer.get_description()


