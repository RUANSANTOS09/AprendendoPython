values = [10, 49.99,199.90, 1500]
conversion = lambda x: x * 5.70
result = list(map(conversion, values))
for numero in result:
    print(round(numero, 2))
