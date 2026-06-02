def pipeline(val):
    valid_values = []
    for x in val:
        if x is not None and x > 0:
            valid_values.append(x)
    unique = set(valid_values)
    return {
        'average': sum(unique) / len(unique),
        'min_value': min(unique),
        'max_value': max(unique)
    }

sales_list = [1000,1000,2000, None, -500, 3000,0, 2000, 1500]
for metric,value in pipeline(sales_list).items():
    print(f'{metric}: {value}')