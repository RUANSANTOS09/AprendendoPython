product = ['notebook,2500\n', 'mouse,50\n', 'teclado,120\n', 'monitor,800']
try:
    manipulator = open('vendas_brutas.txt','w', encoding='utf-8')
except IOError:
    print('Arquivo não encontrado!!!')
else:
    manipulator.writelines(product)
    manipulator.close()



try:
    manipulator = open('vendas_brutas.txt', 'r', encoding='utf-8')
except IOError:
    print('Arquivo não encontrado!!!')
else:
    report = open('relatorio_vendas.txt', 'w', encoding='utf-8')
    for line in manipulator:
        name, price = line.rstrip().split(',')
        new_report =  f'Produto: {name} | Preço: R$ {price}\n'
        report.write(new_report)

    manipulator.close()
    report.close()
