n, m = [int(x) for x in (input().split())]
set1 = set(int(input()) for _ in range(n))
set2 = set(int(input()) for _ in range(m))

print(*set1.intersection(set2), sep = '\n')