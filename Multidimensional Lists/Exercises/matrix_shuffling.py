rows, columns = [int(x) for x in input().split()]
matrix = list([x for x in input().split()] for i in range(rows))

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    action, *coordinates = [int(x) if x.isdigit() else x for x in input().split()]
    if action == 'END':
        break
    if action == 'swap' \
            and len(coordinates) == 4 \
            and {coordinates[0], coordinates[2]}.issubset(valid_rows) \
            and {coordinates[1], coordinates[3]}.issubset(valid_columns):
        r1, c1, r2, c2 = coordinates
        matrix[r1][c1], matrix[r2][c2] = matrix[r2][c2], matrix[r1][c1]
        [print(*row, sep=' ') for row in matrix]
    else:
        print('Invalid input!')

