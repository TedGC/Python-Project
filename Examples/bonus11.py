feet_inches = input('enter feet and inches')


def parse(feetinches):
    parts = feetinches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    return (feet, inches)

def convert(feet, inches):
    meters = feet * 0.3048 + inches * 0.0254
    return meters

feet_inches_tuple = parse(feet_inches)
result = convert(feet_inches_tuple[0], feet_inches_tuple[1])

if result < 1: 
    print("kid is too small")
elif result > 1:
    print("good to go")
else: 
    print("who are you?")
