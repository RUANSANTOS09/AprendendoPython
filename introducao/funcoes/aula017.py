# # Funções
# # Modularizção, Reúso de código, Legibilidade
# def mensagem():
#    print('Hello World')
#    print('Engenheiro de Dados')
#
# mensagem()
#
# # FUnção com argumentos
# def soma(num1,num2):
#   print(num1 + num2)
#
#
# soma(4,4)
#
# def mult (x,y):
#   return x * y
#
# a = 5
# b = 7
# c = mult(a,b)
# print(f'O produto de {a} e {b} é {c}')
#
# def div(k,j):
#     if j != 0:
#         return k / j
#     else:
#       return 'Impossivél dividir um número por zero!'
# if __name__ == '__main__':
#     a = int(input('Digite um número: '))
#     b = int(input('Digite outro número: '))
#     r = div(a,b)
#     print(f'{a} dividido por {b} é igual a {r}')
#
# def quadrado(val):
#     quadrados = []
#     for x in val:
#         quadrados.append(x ** 2)
#     return quadrados










# def contar(caractere,num = 11 ):
#     for i in range (1, num):
#         print(caractere)
x = 5
y = 6
z = 3
def soma_mult(a,b,c = 0):
    if( c == 0):
        return a * b
    else:
        return a + b + c
if __name__ == '__main__':
    res = soma_mult(x,y,z)
    print(res)

#     valores = [2,5,7,9,12]
#     resulados = quadrado(valores)
#     for x in resulados:
#         print(x)