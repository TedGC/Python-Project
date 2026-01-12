import FreeSimpleGUI as fsg
from zip_creator import make_archive

label1 = fsg.Text('select files to compress')
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse('choose', key="files")


label2 = fsg.Text('select destination folder')
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse('choose', key="folder")


compress = fsg.Button('compress')
out_msg = fsg.Text(key='output')

window = fsg.Window('file compressor', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress, out_msg]])

while True: 
    event, values = window.read()
    print(event, values)
    filepaths = values['files'].split(';')
    folder = values['folder']
    make_archive(filepaths, folder)
    window['output'].update(value='completed!')
window.close()
