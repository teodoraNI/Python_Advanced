rows = int(input())
matrix = list([int(x) for x in input().split()] for i in range(rows))
secondary_diagonal_sum = 0
primary_diagonal_sum = 0

for i in range(rows):
    primary_diagonal_sum += matrix[i][i]
    secondary_diagonal_sum += matrix[i][rows-1-i]
print(abs(primary_diagonal_sum - secondary_diagonal_sum))
