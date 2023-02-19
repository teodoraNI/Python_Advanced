rows = int(input())
matrix = list([int(x) for x in input().split()] for i in range(rows))
command = input()

while command != 'END':
    action, row, col, value = [int(x) if x.isdigit() else x for x in command.split()]
    if row not in range(rows) or col not in range(len(matrix[row])):
        print('Invalid coordinates')
    elif action == 'Add':
        matrix[row][col] += value
    elif action == 'Subtract':
        matrix[row][col] -= value
    command = input()
[print(*row, sep=' ') for row in matrix]