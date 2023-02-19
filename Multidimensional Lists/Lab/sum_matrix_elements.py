rows, columns = [int(x) for x in input().split(', ')]
matrix = []
sum_matrix_elements = 0
for i in range(rows):
   matrix.append([int(x) for x in input().split(', ')])

sum_matrix_elements = sum(sum(matrix[row]) for row in range(len(matrix)))

print(sum_matrix_elements)
print(matrix)


