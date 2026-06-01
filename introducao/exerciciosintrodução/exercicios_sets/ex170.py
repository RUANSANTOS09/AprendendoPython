students = {'Maria','Luana','Ana','Fabio','Ruan','Henrique','Paula','Joao','Fabiana','Luiza','Pedro','Lucas','Natielly'}
test1 = {'Maria','Luana','Ana','Fabio','Ruan','Henrique','Paula'}
test2 = {'Joao','Fabiana','Luiza','Ruan','Ana','Henrique','Paula'}
students_who_took_the_test = test1 | test2
print(f'Alunos que entregaram as duas provas: {test1 & test2}')
print(f'Alunos que entregaram somente uma das provas: {test1 ^ test2}')
print(f'Alunos que não entregaram nenhuma prova: {students - students_who_took_the_test}')