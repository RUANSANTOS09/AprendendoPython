import os
dir_actual = os.getcwd()
list_arq =  os.listdir(dir_actual)
for item in list_arq:
    if os.path.isfile(item):
       name,extension = os.path.splitext(item)
       print(f'Nome: {name} | Extensão: {extension}')
    else:
        print('Não é um arquivo!!!!')
