prices_usd = [19.99, 45.50, 120.00, 8.75, 340.00, 55.90]
conversion = [round(value * 5.70,2) for value in prices_usd]
print(conversion)