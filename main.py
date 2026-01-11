filenames = ['doc.txt', 'report.txt', 'presentation.txt']

for file in filenames: 
    file = open(file, 'w')
    file.write("Hello")
    file.close()