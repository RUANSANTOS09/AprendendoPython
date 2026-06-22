files = ['vendas.csv', 'log.txt', 'config.json', 'dados.csv']
for number,name in enumerate(files, start =1):
    if name.endswith('.csv'):
        print(f'Arquivo CSV {number}: {name}')