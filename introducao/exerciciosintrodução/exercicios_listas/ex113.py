lista = []
while True:
    opcao = int(input('[1] Compras\n[2] Sair\nDigite o que deseja: '))
    if(opcao == 1):
        compras = input('Digite sua lista de compras: ')
        lista.append(compras)
    else:
        break

print(f'Lista de compras: {lista}')
