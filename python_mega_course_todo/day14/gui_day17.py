import FreeSimpleGUI as sg
import functions
label = sg.Text("Type a todo")
input_box= sg.InputText(tooltip="Enter a todo",key="todo")
add_button= sg.Button("Add")
w= sg.Window('todo app',
             layout=[[label],
                     [input_box,add_button]],
             font=('Helvetica',15))
while True:
    event, values = w.read()
    print(event)
    print(values)
    if "Add" in event:
        todos=functions.get_todos()
        new_todo=values['todo']+"\n"
        todos.append(new_todo)
        functions.write_todos(todos)
        print(todos)
    if sg.WIN_CLOSED:
        break
w.close()

