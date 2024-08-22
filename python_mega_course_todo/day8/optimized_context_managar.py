

while True:
    cmd = input("Type add or show or edit or exit: ")
    cmd = cmd.strip()

    match cmd:
        case 'add':
            todo = input("enter a todo: ") + "\n"

            # file = open('todos.txt','r')
            # todos= file.readlines()
            # file.close()
            with open('../day7/todos.txt','r') as file:
                todos= file.readlines()
            #no need to close the file it will be automatically close it.... type of file handling
            todos.append(todo)

            with open('../day7/todos.txt','w') as file:
                file.writelines(todos)

        case 'show':
            with open('../day7/todos.txt', 'r') as file:
                todos = file.readlines()

            for index,item in enumerate(todos):
                #removing /n
                item=item.strip("\n")
                row= f"{index+1}-{item}"
                print(row)

        case 'edit':

            num = int(input("number of todo to edit: "))-1

            with open('../day7/todos.txt', 'r') as file:
                todos = file.readlines()

            updated_todo = input ("enter the updated todo")
            todos[num]=updated_todo+'\n'

            with open('../day7/todos.txt','w') as file:
                file.writelines(todos)

        case 'remove':
            index = int(input("enter a number of todo to remove: "))

            with open('../day7/todos.txt', 'r') as file:
                todos = file.readlines()

            todos.pop(index-1)

            with open('../day7/todos.txt','w') as file:
                file.writelines(todos)

            msg = f"todo {todos[index]} has been removed from the list"
            print(msg)

        case 'exit':
            break

print("byee")

