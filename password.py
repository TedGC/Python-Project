password = input('enter the password of your preference: ')
result = {}

if len(password) > 8 :
    #  result.append(True)

    result["length"] = True
else:
    result["length"] = False

digit = False
for i in password:
     if i.isdigit():
        digit = True

result["digit"] = digit

uppercase = False
for i in password:
     if i.isupper():
          uppercase = True

result["uppercase"] = uppercase

print(all(result))

