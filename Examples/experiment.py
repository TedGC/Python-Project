# import glob

# myfiles = glob.glob('file/*.txt')

# for filepath in myfiles: 
#     with open( filepath, 'r') as file: 
#         print(file.read())

# print(myfiles)


# import csv 

# with open('file/weather.txt', 'r') as file:
#     data = list(csv.reader(file))

# city = input('enter your city')

# for row in data: 
#     if row[0] == city:
#         print(row[1])


import webbrowser

user_input = input('enter your term: ')

webbrowser.open('https://google.com/search?q=' + user_input)