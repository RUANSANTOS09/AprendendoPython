num1 = [1, 2, 3, 4, 5, 8]
num2 = [2, 4, 6, 7, 8, 1]
num3 = []
for i in num1:
    if i in num2:
        num3.append(i)

print(num3)