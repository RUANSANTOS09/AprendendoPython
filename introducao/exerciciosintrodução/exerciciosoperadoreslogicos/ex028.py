nota_aluno = int(input('Digite a nota do aluno: '))
verificador = (nota_aluno < 5) or (nota_aluno == 0)
print('O aluno vai para a recuperação? {}'.format(verificador))