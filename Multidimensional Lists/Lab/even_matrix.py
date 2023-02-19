rows = int(input())
even_matrix = []

matrix = list([int(x) for x in input().split(', ')] for i in range(rows))

even_matrix = list([el for el in matrix[i] if el % 2 == 0] for i in range(rows))
# for i in range(len(matrix)):
#     row = []
#     for el in matrix[i]:
#         if el % 2 == 0:
#             row.append(el)
#     even_matrix.append(row)
print(even_matrix)


