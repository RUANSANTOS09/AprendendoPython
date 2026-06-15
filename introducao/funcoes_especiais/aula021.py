# Funções lambda (anônimas)
# Sintaxe:
# lambda argumentos: expressão

# quadrado = lambda x : x ** 2
# for i in range (1,11):
#     print(quadrado(i))

# par = lambda numero: numero % 2 == 0
# while(True):
#     try:
#         verificador = int(input('Digite um número e verfique se ele é par ou impar: '))
#     except ValueError:
#         print('Erro, digite um número')
#     else:
#         if par(verificador) == False:
#             print(f'{verificador} é impar')
#         else:
#             print(f'{verificador} é par')

f_c = lambda f: (f - 32) * 5/9
print(f_c(90))

# função map()
# Sintaxe
# map(função, iterável)

num = [1,2,3,4,5,6,7,8]
dobro = list(map(lambda x : x*2, num)

