from modules import functions

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()

    if user_action.startswith("add"):
        todo = user_action[4:].strip()
        if not todo:
            todo = input("Enter a todo: ").strip()

        if todo:
            todos = functions.get_todos_local()
            todos.append(todo + "\n")
            functions.write_todos(todos)
        else:
            print("Todo is empty.")

    elif user_action.startswith("show"):
        todos = functions.get_todos_local()
        for index, item in enumerate(todos):
            print(f"{index + 1}-{item.strip().capitalize()}")

    elif user_action.startswith("edit"):
        try:
            number = int(user_action.split()[1]) - 1
            todos = functions.get_todos_local()
            new_todo = input("Enter new todo: ").strip()
            if new_todo:
                todos[number] = new_todo + "\n"
                functions.write_todos(todos)
            else:
                print("Todo is empty.")
        except (IndexError, ValueError):
            print("Your command is not valid.")

    elif user_action.startswith("complete"):
        try:
            number = int(user_action.split()[1]) - 1
            todos = functions.get_todos_local()
            todo_to_remove = todos.pop(number).strip("\n")
            functions.write_todos(todos)
            print(f"Todo: '{todo_to_remove}' was removed from the list.")
        except (IndexError, ValueError):
            print("There is no item with that number.")

    elif user_action == "exit":
        break
    else:
        print("Command not valid.")

print("Bye!")