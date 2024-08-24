def get_todos(filepath="../day7/todos.txt"):
    """docstring
    """
    with open(filepath, 'r') as file1:
        todos1 = file1.readlines()
        return todos1

def write_todos(t,filepath="../day7/todos.txt"):
    with open(filepath,'w') as file2:
        file2.writelines(t)
if __name__=="__main__":
    print("Hello")
    print(get_todos())
