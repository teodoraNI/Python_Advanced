rows, columns = [int(x) for x in input().split()]
r = 97 + rows
c = 97 + columns
matrix = []
for i in range(97, r):
    row = []
    for j in range(97, c):
        el = f'{chr(i)}{chr(i+j - 97)}{chr(i)}'
        row.append(el)
    matrix.append(row)
[print(*row, sep=' ') for row in matrix]
