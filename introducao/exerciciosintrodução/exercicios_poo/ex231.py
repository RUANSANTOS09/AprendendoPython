class Students:
    def __init__(self):
        self.__notes = []

    def set_notes(self, notes):
        self.__notes.append(notes)

    def get_average_notes(self):
        return sum(self.__notes) / len(self.__notes)

    def situation(self):
        average = self.get_average_notes()
        if average >= 7:
            print('Aprovado')
        elif average >= 5 and average <= 6.9 :
            print('Em recuperação')
        else:
            print('Reprovado')

my_students = Students()
my_students.set_notes(7)
my_students.set_notes(5)
my_students.set_notes(9)
my_students.set_notes(5)
print(f'Média do aluno: {my_students.get_average_notes()}')
my_students.situation()