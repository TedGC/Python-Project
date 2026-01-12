import json

with open('question.json', 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0 

for question in data:
    print(question['questions_text'])
    for index, alternative in enumerate(question['alternatives']):
        print(index + 1, '-', alternative)
    user_choice = int(input('enter your choice: '))
    question['user_choice'] = user_choice
    if question['user_choice'] == question['correct_answer']:
        score = score + 1

print(score)