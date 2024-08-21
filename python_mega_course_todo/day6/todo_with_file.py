
while True:
    cmd = input("Type add or show or edit or exit: ")
    cmd = cmd.strip()

    match cmd:
        case 'add':
            todo = input("enter a todo: ") + "\n"

            file = open('todos.txt','r')
            todos= file.readlines()
            file.close()

            todos.append(todo)

            file = open('todos.txt','w')
            file.writelines(todos)
            file.close()

        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()

            for index,item in enumerate(todos):
                #print (index, item)
                #f string
                row= f"{index}-{item}"
                print(row)

        case 'edit':
            num = int(input("number of todo to edit: "))
            updated_todo = input ("enter the updated todo")
            todos[num]=updated_todo

        case 'exit':
            break

print("byee")

