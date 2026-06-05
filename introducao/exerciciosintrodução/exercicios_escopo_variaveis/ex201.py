var_global_status = 'Disconnect'
print(var_global_status)
def connect():
    global var_global_status
    var_global_status = 'Connect'
    print(var_global_status)

connect()
