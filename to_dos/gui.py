import functions 
import FreeSimpleGUI as fsg

label = fsg.Text('type in a to-do')
input_box = fsg.InputText(tooltip='enter todo')
add_button = fsg.Button('Add')

window = fsg.Window('To Do App', layout=[[label], [input_box, add_button]])
window.read() 
window.close()