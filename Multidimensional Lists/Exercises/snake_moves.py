from collections import deque

rows, columns = [int(x) for x in input().split()]
snake = deque(input())
matrix = list(['' for j in range(columns)] for i in range(rows))
for i in range(rows):
    if i % 2 == 0:
        for j in range(columns):
            matrix[i][j] = snake[0]
            snake.append(snake.popleft())
    else:
        for j in range(columns-1, -1, -1):
            matrix[i][j] = snake[0]
            snake.append(snake.popleft())
[print(*row, sep ='') for row in matrix]