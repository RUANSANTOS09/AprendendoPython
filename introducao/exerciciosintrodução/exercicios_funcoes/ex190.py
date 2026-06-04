def create_user(name,email):
    return {'name':name,'email':email}



def add_age(val, age):
    val['age'] = age
    return val

user = create_user('Ruan','criologil')
user_with_age = add_age(user, 15)
print(user_with_age)