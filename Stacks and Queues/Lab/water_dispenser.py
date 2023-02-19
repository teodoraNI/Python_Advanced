from collections import deque

water_quantity = int(input())
data = input()
names = deque()
while data != 'Start':
    names.append(data)
    data = input()
command = input()
while command != 'End':
    if command.isdigit():
        if water_quantity >= int(command):
            water_quantity -= int(command)
            print(f'{names.popleft()} got water')
        else:
            print(f'{names.popleft()} must wait')
    elif command.startswith('refill'):
        liters = int(command.split()[1])
        water_quantity += liters
    command = input()
print(f'{water_quantity} liters left')

