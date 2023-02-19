string = input()
n = int(input())
field = []
player_pos = ()
for i in range(n):
    field.append(list(input()))
    if 'P' in field[i]:
        player_pos = (i,field[i].index('P'))

moves = {
    "up":(-1,0),
    "down":(1,0),
    "left":(0,-1),
    "right":(0,1)
}

for i in range(int(input())):
    command = input()
    r = moves[command][0] + player_pos[0]
    c = moves[command][1] + player_pos[1]
    if r in range(n) and c in range(n):
        field[player_pos[0]][player_pos[1]] = '-'
        player_pos = (r,c)
        if field[r][c].isalpha():
            string += field[r][c]
            field[r][c] = 'P'
    else:
        if string:
            string = string[:-1]

print(string)
[print(''.join(x)) for x in field]
