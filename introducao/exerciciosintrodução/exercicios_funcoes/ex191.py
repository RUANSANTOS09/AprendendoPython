def create_user(name,age):
    return {'name':name,'age':age}
def update_email(val,email):
    val['email'] = email
    return val

user = create_user('Ruan',18)
user_with_new_email = update_email(user,'criologill@gmail.com')
print(user_with_new_email)