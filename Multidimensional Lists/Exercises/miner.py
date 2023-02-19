n = int(input())
commands = input().split()
matrix = []
directions = {
    'left': (0,-1),
    'right': (0,1),
    'up': (-1,0),
    'down': (1,0)
}
coals, total_coals = 0, 0
valid_range = range(0,n)

for r in range(n):
    matrix.append(input().split())
    if 's' in matrix[r]:
        miner_pos = [r,matrix[r].index('s')]
    total_coals += matrix[r].count('c')

for command in commands:
    r, c = miner_pos[0] + directions[command][0], miner_pos[1] + directions[command][1]
    if r not in valid_range or c not in valid_range:
        continue
    miner_pos = [r,c]
    if matrix[r][c] == 'e':
        print(f'Game over! ({r}, {c})')
        exit()
    elif matrix[r][c] == 'c':
        coals += 1
        matrix[r][c] = '*'
        if coals == total_coals:
            print(f'You collected all coal! ({r}, {c})')
            exit()
print(f'{total_coals - coals} pieces of coal left. ({miner_pos[0]}, {miner_pos[1]})')




