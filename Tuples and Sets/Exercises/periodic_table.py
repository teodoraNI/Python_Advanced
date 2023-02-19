elements = []
for _ in range(int(input())):
    elements.extend(input().split())
result = set(elements)
print(*result, sep='\n')