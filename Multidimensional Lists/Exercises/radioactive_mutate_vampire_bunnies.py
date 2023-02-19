def bunnies_moves(matrix):
    bunnies = []
    for row in range(rows):
        for column in range(columns):
            if matrix[row][column] == 'B':
                bunnies.append((row, column))
    for bunnie in bunnies:
        for key, values in moves.items():
            if bunnie[0]+moves[key][0] in range(rows) and bunnie[1]+moves[key][1] in range(columns):
                matrix[bunnie[0]+moves[key][0]][bunnie[1]+moves[key][1]] = 'B'


rows, columns = [int(x) for x in input().split()]
lair = list([x for x in list(input())] for i in range(rows))
commands = list(input())
moves = {
    'L':(0,-1),
    'R':(0,1),
    'U':(-1,0),
    'D':(1,0)
}

for row in range(rows):
    if 'P' in lair[row]:
        player_pos = [row,lair[row].index('P')]

for command in commands:
    r = moves[command][0] + player_pos[0]
    c = moves[command][1] + player_pos[1]
    lair[player_pos[0]][player_pos[1]] = '.'
    bunnies_moves(lair)
    if r not in range(rows) or c not in range(columns):
        [print(''.join(row)) for row in lair]
        print(f'won: {player_pos[0]} {player_pos[1]}')
        break
    player_pos = [r, c]
    if lair[r][c] == 'B':
        [print(''.join(row)) for row in lair]
        print(f'dead: {r} {c}')
        break



