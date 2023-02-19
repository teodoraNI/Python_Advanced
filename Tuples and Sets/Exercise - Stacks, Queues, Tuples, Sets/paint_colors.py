from collections import deque
parts = deque(input().split())
colors = ['red', 'yellow', 'blue', 'orange', 'purple', 'green']
secondary_colors = {
    'orange': {'yellow', 'red'},
    'purple': {'red', 'blue'},
    'green': {'blue', 'yellow'}
}
found_colors = []
while parts:
    el1 = parts.popleft()
    el2 = parts.pop() if parts else ''
    for color in (el1 + el2, el2 + el1):
        if color in colors:
            found_colors.append(color)
            break
    else:
        for el in (el1[:-1], el2[:-1]):
            if el:
                parts.insert(len(parts) // 2, el)
for color in set(secondary_colors.keys()).intersection(found_colors):
    if not secondary_colors[color].issubset(found_colors):
        found_colors.remove(color)
print(found_colors)

