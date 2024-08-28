import FreeSimpleGUI as sg
label = sg.Text("Type a todo")
input_box= sg.InputText(tooltip="Enter a todo")
add_button= sg.Button("Add")
w= sg.Window('todo app', layout=[[label],[input_box,add_button]])
w.read()
w.close()

# import FreeSimpleGUI as sg                        # Part 1 - The import
#
# # Define the window's contents
# layout = [  [sg.Text("What's your name?")],     # Part 2 - The Layout
#             [sg.Input()],
#             [sg.Button('Ok')] ]
#
# # Create the window
# window = sg.Window('Window Title', layout)      # Part 3 - Window Defintion
#
# # Display and interact with the Window
# event, values = window.read()                   # Part 4 - Event loop or Window.read call
#
# # Do something with the information gathered
# print('Hello', values[0], "! Thanks for trying FreeSimpleGUI")
#
# # Finish up by removing from the screen
# window.close()