nome = input('Digite o nome do funcionario: ')
salario = float(input('Qual é o salário do funcionario? R$'))
aumento_porcentagem = float(input('Digite o acrecimo em porcetagem: '))
conta = salario + (salario * aumento_porcentagem)
print('O funcionário {}, que ganhava {:.2f}R$, com {}% de aumento, passa a receber {:.2f}R$'.format(nome,salario, aumento_porcentagem, conta))

