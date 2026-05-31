filter_employee = 0
employee_data = {
    'Joana': 1500,
    'Leandro': 1800,
    'Fabio': 5000,
    'Junior': 15000
}
for employee, wage in employee_data.items():
    if wage > 3000:
        filter_employee += 1
        print(f'{employee}: {wage}')
print(f'{filter_employee} funcionários recebem mais de 3000 reais')