def move(direction, steps):
    r = my_pos[0] + (directions[direction][0])*steps
    c = my_pos[1] + (directions[direction][1])*steps
    if r not in range(5) or c not in range(5):
        return my_pos
    if matrix[r][c] == 'x':
        return my_pos
    return (r,c)


def shoot(direction):
    r = my_pos[0] + directions[direction][0]
    c = my_pos[1] + directions[direction][1]
    while r in range(5) and c in range(5):
        if matrix[r][c] == 'x':
            matrix[r][c] = '.'
            return [r,c]
        r+=directions[direction][0]
        c+=directions[direction][1]


matrix = []
shooted_targets = []
targets = 0
my_pos = []

directions = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1)
}
for row in range(5):
    matrix.append(input().split())
    if 'A' in matrix[row]:
        my_pos = (row, matrix[row].index('A'))
        matrix[my_pos[0]][my_pos[1]] = '.'
    targets += matrix[row].count('x')

for _ in range(int(input())):
    command = input().split()
    if command[0] == 'move':
        my_pos = move(command[1], int(command[2]))
    elif command[0] == 'shoot':
        target_down_pos = shoot(command[1])
        if target_down_pos:
            shooted_targets.append(target_down_pos)
            targets -=1
            if targets ==0:
                print(f'Training completed! All {len(shooted_targets)} targets hit.')
                break
if targets:
    print(f'Training not completed! {targets} targets left.')
print(*shooted_targets, sep='\n')
