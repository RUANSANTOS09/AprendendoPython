contador_funcionario = 1
soma_salario = 0
while(contador_funcionario <= 6):
    salario = float(input(f'Digite o salário do funcionario {contador_funcionario} R$ '))
    contador_funcionario += 1
    soma_salario += salario

media = soma_salario / 6
print(f'A média salárial dos 6 funcionários é igual a R${media:.2f}')