nota_aluno = float(input('Digite a nota do aluno: '))
if nota_aluno >= 7:
    print('Aprovado')
elif(nota_aluno >= 5 and nota_aluno <= 6):
    print('Recuperação')
else:
    print('Reprovado')