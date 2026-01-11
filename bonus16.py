import FreeSimpleGUI as fsg


label1 = fsg.Text('select files to compress')
input1 = fsg.Input()
choose_button1 = fsg.FileBrowse('choose')


label2 = fsg.Text('select destination folder')
input2 = fsg.Input()
choose_button2 = fsg.FolderBrowse('choose')

compress = fsg.Button('compress')

window = fsg.Window('file compressor', layout=[[label1, input1, choose_button1], [label2, input2, choose_button2], [compress]])
window.read()
window.close()