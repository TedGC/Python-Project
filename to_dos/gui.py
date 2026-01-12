import functions 
import FreeSimpleGUI as fsg
import time 

label = fsg.Text('type in a to-do')
input_box = fsg.InputText(tooltip='enter todo', key='todo')
add_button = fsg.Button('Add')
list_box = fsg.Listbox(values=functions.get_todos(), enable_events=True, key='todos', size=[45, 10])

clock =fsg.Text('', key='clock')
edit_button = fsg.Button('Edit')
complete_button = fsg.Button('Complete')
exit_button = fsg.Button('Exit')

window = fsg.Window('To Do App', 
                    layout=[
                    [clock],    
                    [label], 
                    [input_box, add_button],
                    [list_box, edit_button],
                    [complete_button],
                    [exit_button]],
                    font=('Helvetica', 20))


while True: 
    event, values = window.read(timeout=200) 
    window['clock'].update(value=time.strftiem("%b %d, %Y %H:%M:%S"))
    print(event)
    print(values)
    match event:
        case 'Add': 
            todos = functions.get_todos()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                fsg.popup('select an item', font=('Helvetica', 20))
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case fsg.WIN_CLOSED: 
            break 
window.close()