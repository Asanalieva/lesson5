import datetime

todoList = [] #massive

try:
    while True: #to check
        print()
        operation = int(input('Add todo(1)? or show todos(2) '))
        print()
        if operation == 1:
            todo = input("Write task: ")
            date = datetime.datetime.now()
            todoList.append({
                'todo': todo,
                'date': date
            })
            print("Task added successfully!")
            print()
        elif operation == 2:
            for todo in todoList:
                print(f'Task: {todo["todo"]}\ndate of creation: {todo["date"]}')
                print()

except ValueError:
    print('Write an integer!')
except:
    print('Error')
finally:
    print('Goodbye!')





