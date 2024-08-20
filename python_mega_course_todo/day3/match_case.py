todos = []
while True:
    cmd = input("Type add or show: ")

    match cmd:
        case 'add':
            todo = input("enter a todo: ")
            todos.append(todo)
        case 'show':
            print (todos)

