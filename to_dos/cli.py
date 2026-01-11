import functions

while True:
    user_action = input("Enter your todo action (add, show, complete, edit or exit): ")
    user_action = user_action.strip()

    # match user_action:


        # case "add":

    # if 'add' in user_action or 'new' in user_action:
    if user_action.startswith('add'):
            # todo = input ("Enter a todo item: ") + '\n'
            todo = user_action[4:]
            # file = open('todos.txt', 'r')
            # todos = file.readlines()
            # file.close()

            todos = functions.get_todos()

            todos.append(todo + '\n')

            #'with' method allows no further use of file.close()
            # with open('todos.txt', 'w') as file:
            #     todos = file.writelines(todos)

            functions.write_todos(todos, 'todos.txt')
    elif user_action.startswith('show'):
            todos = functions.get_todos()

            new_todos = []

            # for item in todos: 
            #     new_item = item.strip('\n')
            #     new_todos.append(new_item)

            #list comprehension emthodology 
            # new_todos = [item.streip('\n' for item in todos)


            for index, item in enumerate(todos):
                item = item.strip('\n').capitalize()
                new_item = f"{index + 1}-{item}"
                print(new_item)

    elif user_action.startswith('exist'):
            break
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1  # Adjust for zero-based index

            todos = functions.get_todos()

            new_todo = input("Enter the new todo item: ")            
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, 'todos.txt')
        except ValueError: 
             print('not valid')
            #  user_action = input("Enter your todo action (add, show, complete, edit or exit): ")
            #  user_action = user_action.strip()
             continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
        
            todos = functions.get_todos()

            index = number - 1 
            item_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos(todos, 'todos.txt')

            message = f"you have successfully removed {item_to_remove}"
            print(message)
        except IndexError:
            print('not valid command')
            continue
    else:
        print("Invalid action. Please enter add, show, or exit.")
    


