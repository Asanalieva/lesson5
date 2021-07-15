dictionary = {
    'jack': 'jack is name',
    'john': 'john',
    'key': 'value'
}

# print(dictionary['jack'])
#key and value write key to get value тип данных  = dict,mass,str,int

user = {
    'name': 'John',
    'age': 18,
}
user2 = {
    'name': 'Jol',
    'age': 24,
}
print(user.keys())
print(user.values())

print(user)
user.clear()
print(user)
user['name'] = 'Dilbara'
print(user)
user['name2'] = 'Maruf' #create new key or
print(user)
print(user.pop('name2'))
print(user)
print(user.get('name'))
user3 = user.copy()
print(user)
user3 = user.popitem() #как кортедж
print('this', user3)
test = ('name',1212,user,121) #кортедж
for key in user:
    print(key, user[key]) #to get key and value

mass = [1,2,3,4,5]
for num in range(3):
    print(mass)
#complate the code