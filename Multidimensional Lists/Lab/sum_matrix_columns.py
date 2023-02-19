rows, columns = [int(x) for x in input().split(', ')]
result = []
matrix = list([int(x) for x in input().split()] for i in range(rows))
for i in range(columns):
    sum_column = 0
    for j in range(rows):
        sum_column += matrix[j][i]
    result.append(sum_column)
print(*result, sep='\n')