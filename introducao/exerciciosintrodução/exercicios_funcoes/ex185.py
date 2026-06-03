def multiply_list(val, mult = 2):
    new_list = []
    for num in val:
        num = num * mult
        new_list.append(num)
    return new_list
list_number = [1,2,3,4,5,6,7,8,9,10]
print(multiply_list(list_number))