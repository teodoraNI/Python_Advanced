matrix = list([int(x) for x in line.split()] for line in input().split('|'))
list_result = []
[list_result.extend(matrix[row]) for row in range(len(matrix)-1, -1, -1)]
print(*list_result)


