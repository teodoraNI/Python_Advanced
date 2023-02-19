n = int(input())
matrix = list([int(x) if x.isdigit() else x for x in input().split()] for i in range(n))
moves = {
    'up':(-1,0),
    'down':(1,0),
    'left':(0,-1),
    'right':(0,1)
}
for row in range(n):
    if 'A' in matrix[row]:
        r, c = row, matrix[row].index('A')
matrix[r][c] = '*'
tea = 0
while tea < 10:
    command = input()
    r += moves[command][0]
    c += + moves[command][1]
    alice_pos = (r,c)
    if r not in range(n) or c not in range(n):
        break
    if matrix[r][c] == 'R':
        matrix[r][c] = '*'
        break
    if matrix[r][c] == '.':
        matrix[r][c] = '*'
    elif matrix[r][c] == '*':
        continue
    else:
        tea += matrix[r][c]
        matrix[r][c] = '*'

if tea<10:
    print("Alice didn't make it to the tea party.")
else:
    print("She did it! She went to the party.")
[print(*row) for row in matrix]

