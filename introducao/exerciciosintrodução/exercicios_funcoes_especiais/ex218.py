from functools import reduce

transitions = [250.0, 520.99, 89.90, 1200.0, 75.0]
total_sales = reduce(lambda x,y: x+y, transitions)
print(f'Total de vendas do dia: R$ {round(total_sales,2)}')
