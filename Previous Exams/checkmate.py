chess_field = []
king_pos = ()
queens = []
for i in range(8):
    chess_field.append(input().split())
    if 'K' in chess_field[i]:
        x = i
        y = chess_field[i].index('K')
        king_pos = (x,y)
moves = [
    (-1,0),
    (1,0),
    (0,-1),
    (0,1),
    (-1,1),
    (1,1),
    (1,-1),
    (-1,-1)
]

for move in moves:
    queen_found = False
    king_pos = (x,y)
    r = king_pos[0] + move[0]
    c = king_pos[1] + move[1]
    while r in range(8) and c in range(8):
        if chess_field[r][c] == 'Q':
            queens.append([r,c])
            queen_found = True
            break
        else:
            r += move[0]
            c += move[1]
if queens:
    print(*queens, sep='\n')
else:
    print("The king is safe!")



