todos = ['one', 'two', 'three', 'four']

from sys import version
print(version)
while True:
    cmd = input("Type add or show or edit or exit: ")
    cmd = cmd.strip()
    match cmd:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print (item)
        case 'edit':
            num = int(input("number of todo to edit: "))
            updated_todo = input ("enter the updated todo")
            todos[num]=updated_todo
        case 'exit':
            break
print("byee")

