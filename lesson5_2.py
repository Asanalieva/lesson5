user = {
    'name': 'John',
    'age': 18,
}
user2 = {
    'name': 'Jolie',
    'age': 24,
}
users = []
users.append(user)
users.append(user2)
print(users)
for user in users:
    print(f'name: {user["name"]} \nage: {user["age"]}\n ') #f format to use and not see {}