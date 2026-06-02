def summary_date_set(val):
    return {
        'average': sum(val) / len(val),
        'max_value': max(val),
        'min_value': min(val),
        'total_records': len(val)
            }

sales_list = [2000,20000,5000,4000]
for metric, value in summary_date_set(sales_list).items():
    print(f'{metric} : {value} ')
