n = int(input())
matrix = list([x for x in list(input())] for i in range(n))
food = 0
moves = {
    'left':(0,-1),
    'right':(0,1),
    'up':(-1,0),
    'down':(1,0)
}
burrows = []
for row in range(n):
    for column in range(n):
        if matrix[row][column] == 'S':
            snake_pos = [row, column]
        elif matrix[row][column] == 'B':
            burrows.append((row, column))
while food < 10:
    command = input()
    matrix[snake_pos[0]][snake_pos[1]] = '.'
    r = moves[command][0]+snake_pos[0]
    c = moves[command][1]+snake_pos[1]
    snake_pos = [r,c]
    if r not in range(n) or c not in range(n):
        print('Game over!')
        break
    if matrix[r][c] == '*':
        matrix[r][c] = 'S'
        food += 1
    elif matrix[r][c] == 'B':
        matrix[r][c] = '.'
        burrows.remove((r,c))
        snake_pos = [burrows[0][0],burrows[0][1]]
        matrix[burrows[0][0]][burrows[0][1]] == 'S'

if food >= 10:
    print('You won! You fed the snake.')
print(f'Food eaten: {food}')
[print(''.join(row)) for row in matrix]

