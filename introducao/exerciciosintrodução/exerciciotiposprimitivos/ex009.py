nomeAluno = str(input('Digite o nome do aluno: '))
notaPrimeiraUnidade1 = float(input('Digite a primeira nota: '))
notaSegundaUnidade2 = float(input('Digite a segunda nota: '))
notaTerceiraUnidade = float(input('Digite a terceira nota: '))
media = (notaPrimeiraUnidade1 + notaSegundaUnidade2 + notaTerceiraUnidade) / 3
print('A media do aluno {} é igual {:.1f}'.format(nomeAluno,media))