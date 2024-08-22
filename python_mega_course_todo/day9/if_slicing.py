while True:
    cmd = input("Type add or show or edit or remove or exit: ")
    cmd = cmd.strip()

    if 'add' in cmd:
        todo=cmd[4:]

        with open('../day7/todos.txt','r') as file:
            todos= file.readlines()
        todos.append(todo)
        print(todos)
        with open('../day7/todos.txt','w') as file:
            file.writelines(todos)

    elif 'show' in cmd:
        with open('../day7/todos.txt', 'r') as file:
            todos = file.readlines()

        for index,item in enumerate(todos):
            #removing /n
            item=item.strip("\n")
            row= f"{index+1}-{item}"
            print(row)

    elif 'edit' in cmd:

        #num = int(input("number of todo to edit: "))-1
        num=int(cmd[5])-1
        with open('../day7/todos.txt', 'r') as file:
            todos = file.readlines()

        #updated_todo = input ("enter the updated todo")
        updated_todo = cmd [7:]
        todos[num]=updated_todo+'\n'

        with open('../day7/todos.txt','w') as file:
            file.writelines(todos)

    elif 'remove' in cmd:
        index= int(cmd[7:])
        with open('../day7/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.pop(index-1)

        with open('../day7/todos.txt','w') as file:
            file.writelines(todos)

        msg = f"todo {todos[index]} has been removed from the list"
        print(msg)

    elif 'exit' in cmd:
        break
    else:
        print("command is not valid")

print("byee")

