rows = int(input())
flatten_matrix = []

matrix = list([int(x) for x in input().split(', ')] for i in range(rows))
for i in range(rows):
    flatten_matrix.extend(matrix[i])
print(flatten_matrix)