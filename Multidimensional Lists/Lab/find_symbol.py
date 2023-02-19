rows = int(input())
matrix = list([x for x in input()] for i in range(rows))
symbol = input()

for i in range(rows):
    for j in range(rows):
        if matrix[i][j] == symbol:
            result = (i, j)
            print(result)
            exit()
print(f'{symbol} does not occur in the matrix')

