rows = int(input())
matrix = list([int(x) for x in input().split()] for i in range(rows))

primary_diagonal = sum(matrix[i][i] for i in range(rows))
print(primary_diagonal)

