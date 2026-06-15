from functools import reduce
product = ['  Notebook ', 'CELULAR', ' Mouse ', 'TECLADO', '  Monitor', 'webcam  ']
transitions = [250.0, -30.0, 0, 520.99, -5.0, 89.90, 1200.0, -0.01, 75.0]

standardizing_data = list(map(lambda x: x.strip().lower(), product))

filtering_data = list(filter(lambda x: x > 0, transitions))

conversion = lambda x: round(x * 5.70,2)
result = list(map(conversion, filtering_data))
total_sales = reduce(lambda x,y: x + y, result)

print(f'Produtos: {standardizing_data}')
print(f'Transações válidas (R$): {result}')
print(f'Total de vendas do dia: R$ {round(total_sales,2)}')
