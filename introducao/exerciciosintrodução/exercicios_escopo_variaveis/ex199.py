var_global_count = 0
def write_text():
    global var_global_count
    var_global_count += 1
    print(var_global_count)

write_text()
write_text()
write_text()
print(f'Valor final: {var_global_count}')