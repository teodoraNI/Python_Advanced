import os
command = input()
while command != 'End':
    action, name, *others = command.split('-')
    if action == 'Create':
        file = open(f"{name}",'w')
        file.close()
    elif action == 'Add':
        file = open(f"{name}", 'a')
        file.write(f"{others[0]}\n")
        file.close()
    elif action == 'Replace':
        try:
            with open(f"{name}", 'r') as file:
                text = file.read()
            text = text.replace(others[0], others[1])
            with open(f"{name}", 'w') as file:
                file.write(text)
        except FileNotFoundError:
            print("An error occurred")
    elif action == 'Delete':
        try:
            os.remove(name)
        except FileNotFoundError:
            print("An error occurred")
    command = input()