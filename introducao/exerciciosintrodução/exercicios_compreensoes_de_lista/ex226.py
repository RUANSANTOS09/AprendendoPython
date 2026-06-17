prices = [100.0, 250.0, 80.0, 430.0, 60.0]
discounts = lambda x: x - ( x * 0.10)
apply_discount = [discounts(x) for x in prices]
print(apply_discount)