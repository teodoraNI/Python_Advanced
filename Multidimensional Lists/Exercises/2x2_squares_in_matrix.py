rows, columns = [int(x) for x in input().split()]
matrix = list([x for x in input().split()] for i in range(rows))
counter = 0
suitable = True

for i in range(columns - 1):
    for j in range(rows - 1):
        suitable = True
        element = matrix[j][i]
        for r in range(2):
            for c in range(2):
                current_element = matrix[r+j][c+i]
                if current_element != element:
                    suitable = False
                    break
            if not suitable:
                break
        if not suitable:
            continue
        else:
            counter += 1
print(counter)
