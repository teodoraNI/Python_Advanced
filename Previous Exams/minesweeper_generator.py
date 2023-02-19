n = int(input())
field = []
for i in range(n):
    field.append([])
    for j in range(n):
        field[i].append(0)
bombs = int(input())
for _ in range(bombs):
    pos = [int(x) for x in input() if x.isdigit()]
    field[pos[0]][pos[1]] = '*'

dirs = [
    (0,1),
    (0,-1),
    (-1,0),
    (1,0),
    (-1,1),
    (-1,-1),
    (1,-1),
    (1,1)
]

for i in range(n):
    for j in range(n):
        if field[i][j] != '*':
            for dir in dirs:
                x = dir[0]+i
                y = dir[1]+j
                if x in range(n) and y in range(n):
                    if field[x][y] == '*':
                        field[i][j] += 1

[print(*row, sep=' ') for row in field]