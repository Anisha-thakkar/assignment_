import FreeSimpleGUI as sg
l1 = sg.Text("Select file to compress: ")
input_box1= sg.InputText(tooltip="Choose file")
b1= sg.FileBrowse("Choose")
l2 = sg.Text("Select destination folder: ")
input_box2= sg.InputText(tooltip="Choose folder")
b2= sg.FolderBrowse("Choose")
b3= sg.Button("Compress")

w= sg.Window('file zipper', layout=[[l1,input_box1,b1],[l2,input_box2,b2],[b3]])
w.read()
w.close()