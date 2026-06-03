def filter_by_value(val, min = 100,max = 5000):
    valid_values = []
    for num in val:
        if num >= min and num <= max:
             valid_values.append(num)
    return valid_values

list_number = [200,1000,4000,6000,8000,5000,100,200]
print(filter_by_value(list_number))
print(filter_by_value(list_number,1000,5000))