from collections import deque

males = [int(x) for x in input().split()]
females = deque([int(x) for x in input().split()])
matches = 0

while males and females:
    if males[-1] <= 0:
        males.pop()
        continue
    if females[0] <= 0:
        females.popleft()
        continue
    if males[-1] % 25 == 0:
        for _ in range(2):
            if males:
                males.pop()
        continue
    if females[0] % 25 == 0:
        for _ in range(2):
            if females:
                females.popleft()
        continue
    if females.popleft() == males[-1]:
        males.pop()
        matches += 1
    else:
        males[-1] -= 2

print(f"Matches: {matches}")
if males:
    print("Males left: ", end = '')
    print(*reversed(males), sep=', ')
else:
    print("Males left: none")
if females:
    print("Females left: ", end = '')
    print(*females, sep = ', ')
else:
    print("Females left: none")
