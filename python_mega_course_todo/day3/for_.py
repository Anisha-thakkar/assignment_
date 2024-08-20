todos = []

from sys import version
print(version)
while True:
    cmd = input("Type add or show or exit: ")
    cmd = cmd.strip()
    match cmd:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show':
            for item in todos:
                print (item)
        case 'exit':
            break
print("byee")

