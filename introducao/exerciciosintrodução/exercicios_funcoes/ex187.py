def count_occurrences(val,vs):
    count = 0
    for num in val:
        if num == vs:
          count += 1
    return count
list_number = [1,1,1,1,5,5,5,5,6,66,7,8,9,10]
list_number2 = [1,1,1,1,5,5,55,7,7,7,7,8,9,10]
print(count_occurrences(list_number, 5))
print(count_occurrences(list_number2, 7))
