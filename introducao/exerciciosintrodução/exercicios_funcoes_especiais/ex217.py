

transitions = [250.0, -30.0, 0, 520.99, -5.0, 89.90, 1200.0, -0.01, 75.0]
clear = list(filter(lambda x: x > 0, transitions))

conversion = lambda x: x * 5.70
result = list(map(conversion, clear))
for number in result:
    print(round(number,2))
