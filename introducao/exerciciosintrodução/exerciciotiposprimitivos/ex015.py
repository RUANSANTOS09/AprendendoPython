nome = input('Digite o nome do funcionario: ')
salario = float(input('Digite o salário do funcionario: '))
aumento_porcentagem = float(input('Digite o acrecimo em porcetagem: '))
conta = salario + (salario * aumento_porcentagem)
print('O funcionario {}, que recebia {}R$, recebera um acrescimo de {} porcento e passara a receber {} R$'.format(nome,salario, aumento_porcentagem, conta))

