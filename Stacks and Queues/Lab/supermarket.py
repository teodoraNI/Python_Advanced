from collections import deque
names = deque()
while True:
    command = input()
    if command == 'Paid':
        while names:
            print(names.popleft())
    elif command == 'End':
        print(f'{len(names)} people remaining.')
        break
    else:
        names.append(command)
