import sys
rows, columns = [int(x) for x in input().split()]
matrix = list([int(x) for x in input().split()] for i in range(rows))
max_sum = - sys.maxsize

for i in range(columns - 2):
    for j in range(rows - 2):
        current_sum = 0
        current_matrix = [[], [], []]
        for r in range(3):
            for c in range(3):
                current_matrix[r].append(matrix[r+j][c+i])
                current_sum += matrix[r+j][c+i]
        if current_sum > max_sum:
            max_sum = current_sum
            searched_matrix = current_matrix
print(f'Sum = {max_sum}')
[print(*row, sep=' ') for row in searched_matrix]
