presents = int(input())
m = int(input())
matrix = []
santa_pos = []
nice_kids_with_presents = 0
for row in range(m):
    matrix.append(input().split())
    if 'S' in matrix[row]:
        santa_pos = [row, matrix[row].index('S')]
moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1)
}
command = input()
while command != 'Christmas morning' and presents > 0:
    r = santa_pos[0] + moves[command][0]
    c= santa_pos[1] + moves[command][1]
    if r in range(m) and c in range(m):
        matrix[santa_pos[0]][santa_pos[1]] = '-'
        santa_pos = [r,c]
        if matrix[r][c] in 'X-':
            matrix[r][c] = 'S'
        elif matrix[r][c] == 'V':
            matrix[r][c] = 'S'
            presents -= 1
            nice_kids_with_presents += 1
        elif matrix[r][c] == 'C':
            matrix[r][c] = 'S'
            for move in moves:
                r = santa_pos[0] + moves[move][0]
                c = santa_pos[1] + moves[move][1]
                if matrix[r][c] == '-':
                    continue
                elif matrix[r][c] == 'X':
                    presents -= 1
                    matrix[r][c] = '-'
                elif matrix[r][c] == 'V':
                    presents -= 1
                    matrix[r][c] = '-'
                    nice_kids_with_presents += 1
    if presents == 0:
        break
    command = input()
count = sum([(row.count("V")) for row in matrix])
if count > 0 and not presents:
    print('Santa ran out of presents!')
[print(*row) for row in matrix]
if count == 0:
    print(f'Good job, Santa! {nice_kids_with_presents} happy nice kid/s.')
else:
    print(f'No presents for {count} nice kid/s.')








