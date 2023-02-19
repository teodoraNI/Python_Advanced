n = int(input())
matrix = []

for row in range(n):
    matrix.append(input().split())
    if 'B' in matrix[row]:
        a, b = row, matrix[row].index('B')
moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1)
}
max_eggs = 0
direction = None
result_list = []
for move in moves:
    eggs = 0
    bunny_pos = (a, b)
    list_eggs_collectd = []
    while True:
        r = bunny_pos[0] + moves[move][0]
        c = bunny_pos[1] + moves[move][1]
        if r not in range(n) or c not in range(n):
            break
        if matrix[r][c] == 'X':
            break
        else:
            eggs += int(matrix[r][c])
            list_eggs_collectd.append([r,c])
            bunny_pos = (r, c)
    if eggs > max_eggs:
        max_eggs = eggs
        direction = move
        result_list = list_eggs_collectd
print(direction)
print(*result_list, sep='\n')
print(max_eggs)
