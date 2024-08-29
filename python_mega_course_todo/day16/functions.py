def get_todos(filepath="/home/anisha/Assignment/python_mega_course_todo/day16/todos.txt"):
    """docstring
    """
    with open(filepath, 'r') as file1:
        todos1 = file1.readlines()
        return todos1

def write_todos(t,filepath="/home/anisha/Assignment/python_mega_course_todo/day16/todos.txt"):
    with open(filepath,'w') as file2:
        file2.writelines(t)
if __name__=="__main__":
    print("Hello")
    print(get_todos())
