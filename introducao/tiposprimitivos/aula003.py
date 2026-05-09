#Operadores Aritmeticos


print('Soma')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))
soma = num1 + num2
print('A soma entre os numeros {} e {} é igual a {}'.format(num1, num2, soma))

print('Subtração')

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))
sub = num1 - num2
print('A subtração entre os numeros {} e {} é igual a {}'.format(num1, num2, sub))

print('Divisão')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero:'))
divisao = num1 / num2
print('A divisao entre os numeros {} e {} é igual a {}'.format(num1, num2, divisao))

print('Divisao inteira')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))
divisaoInteira = num1 // num2
print('A divisao inteira entre os numeros {} e {} é igual a {}'.format(num1, num2, divisaoInteira))

print('Multiplicação')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))
multiplicacao = num1 * num2
print('A multiplicação entre os numeros {} e {} é igual a: {}'.format(num1, num2, multiplicacao))

print('Resto')
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))
res = num1 % num2
print('O resto da divisao entre os numeros {} e {} é igual a {}'.format(num1, num2, res))

print('Raiz Quadrada')
num1 = int(input('Digite um numero: '))
raiz = num1 ** (1/2)

print('A raiz quadrada do numero {} e igual a {}'.format(num1, raiz))