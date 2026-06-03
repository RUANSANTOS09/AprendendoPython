def invert_list(val,order = False):
    if order == True:
        return sorted(val,reverse = True)
    else:
        return list(reversed(val))

list_number = [1,2,3,4,11,6,0]
print(invert_list(list_number,True))
print(invert_list(list_number))
