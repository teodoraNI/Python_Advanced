n = int(input())
max_intersection = set()
for _ in range(n):
    first, second = input().split('-')
    set1 = set(range(int(first.split(',')[0]), int(first.split(',')[1]) + 1))
    set2 = set(range(int(second.split(',')[0]), int(second.split(',')[1]) + 1))
    set3 = set1.intersection(set2)
    if len(set3)> len(max_intersection):
        max_intersection = set3
print(f"Longest intersection is [", end = '')
print(*max_intersection, sep=', ', end = '')
print(f"] with length {len(max_intersection)}")
