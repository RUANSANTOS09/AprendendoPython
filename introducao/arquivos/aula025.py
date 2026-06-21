# Manipulação de arquivos de texto.

# print(f'\nMétodo read():\n')
# print(manipulador.read())


# print(f'\nMétodo readline():\n')
# print(manipulador.readline())
# print(manipulador.readline())

# print(f'\nMétodo readlines():\n')
# print(manipulador.readlines())
# texto = input('Qual termo deseja procurar no arquivo? ')
#try:
#    manipulador = open('arquivo.txt', 'r', encoding='utf8')
#     for linha in manipulador:
#         linha = linha.rstrip()
#         if texto in linha:
#            print(f'A string foi encontrada!')
#            print(linha)
#         else:
#             print('String não encontrada!')
# except IOError:
#     print('Erro ao ler o arquivo')
# else:
# manipulador.close()

# Escrever em arquivos de texto
# try:
#     manipulador = open('arquivo.txt', 'w', encoding='utf8')
#     manipulador.write('Engenheiro de Dados\n')
#     manipulador.write('Engenheiro de IA.')
# except IOError:
#    print('Erro ao ler o arquivo')
# else:
#     manipulador.close()

# Acrescentando textos
# texto = 'Python é usado em Ciência de dados extensivamente'
# try:
#     manipulador = open('arquivo.txt', 'a', encoding='utf8')
#     manipulador.write(f'\n{texto}')
#
# except IOError:
#    print('Erro ao ler o arquivo')
# else:
#     manipulador.close()

# Criar e gravar o arquivo
frutas = ['Morango\n', 'Uva\n', 'Caju\n', 'Banana\n', 'Amora\n', 'Framboesa\n', 'Graviola']

try:
    manipulador = open('../recursos_finais/frutas.txt', 'w', encoding='utf8')
    manipulador.writelines(frutas)
except IOError:
   print('Erro ao ler o arquivo')
else:
    manipulador.close()

#Ler o arquivo criado
try:
    manipulador = open('../recursos_finais/frutas.txt', 'r', encoding='utf8')
    print(manipulador.read())
except IOError:
    print('Erro ao ler o arquivo')
else:
    manipulador.close()
