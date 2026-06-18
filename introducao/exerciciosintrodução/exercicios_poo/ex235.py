class Employee:
    def __init__ (self,name, base_salary):
        self.__name = name
        self.__salary = base_salary

    def get_salary_total(self):
        return self.__salary

class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        self.__bonus = bonus
        super().__init__(name, base_salary)

    def get_salary_total(self):
        return super().get_salary_total() + self.__bonus


class Director(Manager):
    def __init__(self, name, base_salary, bonus, profit_sharing):
        self.__profit_sharing = profit_sharing
        super().__init__(name, base_salary, bonus)

    def get_salary_total(self):
        return  super().get_salary_total() + self.__profit_sharing


my_director = Director('Ruan', 5000, 1000, 2000)
print(f'Novo salário do diretor R$ {my_director.get_salary_total()}')
