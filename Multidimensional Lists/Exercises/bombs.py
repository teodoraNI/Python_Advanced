rows = int(input())
matrix = list([int(x) for x in input().split()] for i in range(rows))

coordinates = ((int(x) for x in coordinate.split(',')) for coordinate in input().split())

directions = (
    (-1,0),  #up
    (1,0),   #down
    (0,1),   #right
    (0,-1),   #left
    (1,1),   #bottom-right
    (-1,-1),   #top-left
    (1,-1),     #bottom-left
    (-1,1),     #top-right
    (0,0)       # current position
)
for row, col in coordinates:
    if matrix[row][col] <= 0:
        continue
    for x, y in directions:
        r, c = row + x, col + y
        if 0 <= r < rows and 0 <= c < rows:
            matrix[r][c] -= matrix[row][col] if matrix[r][c] > 0 else 0
alive_cells = [x for row in range(rows) for x in matrix[row] if x>0]
sum_alive_cells = sum(alive_cells)
print(f'Alive cells: {len(alive_cells)}')
print(f'Sum: {sum_alive_cells}')
[print(*row, sep=' ') for row in matrix]
