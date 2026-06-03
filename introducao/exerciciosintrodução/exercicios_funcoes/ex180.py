def process_sales(val, tax = 0.15, dis = 0):
    values_valid = []
    for sale in val:
        sale = (sale * (1 + tax)) - dis
        values_valid.append(sale)
    return values_valid
sales_list = [200,3000,4000]
print(process_sales(sales_list))