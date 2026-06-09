name_list = ['Pedro','Luan','Ruan','Victor']
while True:
    try:
        accessing_index = int(input('Digite um numero inteiro para acessar um nome da lista: '))
        print(name_list[accessing_index])
        break
    except IndexError:
        print('Esse indice não existe na lista. Tente novamente!!')
