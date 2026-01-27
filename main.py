def get_todos_local(filepath):
    with open(filepath, "r") as file_local:
        todos_local= file_local.readlines()
    return todos_local


while True:
    # Get user input and strip chars it 
    user_action = input("Type add, show, edit, complete or exit:")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todo = user_action[4:]          
        todos = get_todos_local()
        todos.append(todo + '\n')

        with open("files/todos.txt", "w") as file:
            file.writelines(todos)
                    
    elif user_action.startswith("show"):            
        todos = get_todos_local("todos.txt")

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            print (f"{index + 1}-{item.capitalize()}")
            
    elif user_action.startswith("edit"):
        try:        
            number = int(user_action[5:]) 
            print(number)
            number = number - 1
            todos = get_todos_local("todos.txt")
            
            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + "\n"
        except ValueError:
            print("Your command is not valid.")
            continue

            print("Your command is not valid.")
            continue
        with open("files/todos.txt", "w") as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos_local("todos.txt")
            index = number - 1
            todo_to_remove = todos[index].strip('\n')   
            todos.pop(index)

            with open("files/todos.txt", "w") as file:
                file.writelines(todos)
            message = f"Todo: '{todo_to_remove}' was removed from the list."
            print(message)
        except IndexError:
            print("There is no item with that number.")
            continue
        
        
    elif user_action.startswith("exit"):
        break
    else:
        print("Command not valid.")
print("Bye!")  