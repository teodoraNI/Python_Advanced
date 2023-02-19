n, m = input().split()
field = []
for i in range(int(n)):
    field.append(input().split())
    if 'B' in field[i]:
        my_pos = (i, field[i].index('B'))
touched_opponents = 0
moves = 0
directions = {
    'left':(0,-1),
    'right':(0,1),
    'up':(-1,0),
    'down':(1,0)
}
command = input()
while command != 'Finish':
    r = my_pos[0] + directions[command][0]
    c = my_pos[1] + directions[command][1]
    if r in range(int(n)) and c in range(int(m)):
        if field[r][c] == '-':
            moves += 1
            field[my_pos[0]][my_pos[1]] = '-'
            my_pos = (r,c)
            field[r][c] = 'B'
        elif field[r][c] == 'P':
            moves += 1
            touched_opponents += 1
            if touched_opponents == 3:
                break
            field[r][c] = '-'
            my_pos = (r,c)
    command = input()

print(f"Game over!\nTouched opponents: {touched_opponents} Moves made: {moves}")
