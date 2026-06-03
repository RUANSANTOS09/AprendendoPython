def calculate_discount(val,per = 0.1):
    return val - (val * per)

value = 500
print(calculate_discount(value))