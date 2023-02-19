def get_magic_triangle(n):
    triangle = [[1],[1,1]]
    for i in range(2, n):
        triangle.append([1])
        for j in range(i-1):
            triangle[i].append(triangle[i-1][j] + triangle[i-1][j+1])
        triangle[i].append(1)
    return triangle

get_magic_triangle(2)

