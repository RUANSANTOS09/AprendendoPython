var_global_name = 'Ruan'
def write_text():
    global var_global_name
    var_global_name = 'Isabela'
    print(var_global_name)

if __name__ == '__main__':
    write_text()
    print(var_global_name)