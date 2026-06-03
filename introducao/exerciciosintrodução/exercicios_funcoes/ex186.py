def filter_largest(val, vl = 10):
    values_valid = []
    for num in val:
       if num > vl:
           values_valid.append(num)
    return values_valid
list_number = [10,20,30,40,50]
print(filter_largest(list_number))