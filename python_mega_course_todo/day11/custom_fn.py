def get_todos():
    with open('../day7/todos.txt', 'r') as file1:
        todos1 = file1.readlines()
        return todos1

def write_todos(t):
    with open('../day7/todos.txt','w') as file2:
                file2.writelines(t)

while True:
    cmd = input("Type add or show or edit or remove or exit: ")
    cmd = cmd.strip()

    if cmd.startswith('add'):
        todo=cmd[4:]

        todos= get_todos()

        todos.append(todo+"\n")
        print(todos)

        write_todos(todos)

    elif cmd.startswith('show'):
        todos= get_todos()

        for index,item in enumerate(todos):
            #removing /n
            item=item.strip("\n")
            row= f"{index+1}-{item}"
            print(row)

    elif cmd.startswith('edit'):
        try:
            #num = int(input("number of todo to edit: "))-1
            num=int(cmd[5])-1
            todos= get_todos()

            #updated_todo = input ("enter the updated todo")
            updated_todo = cmd [7:]
            todos[num]=updated_todo+'\n'

            write_todos(todos)

        except ValueError:
            print("command is not valid")
            cmd = input("Type add or show or edit or remove or exit: ")
            cmd = cmd.strip()

    elif cmd.startswith('remove'):
        try:
            index= int(cmd[7:])
            todos= get_todos()

            todos.pop(index-1)

            write_todos(todos)
        except IndexError:
            print("Value out of index")
            continue

        # msg = f"todo {todos[index-2]} has been removed from the list"
        # print(msg)

    elif cmd.startswith('exit'):
        break
    else:
        print("command is not valid")

print("byee")