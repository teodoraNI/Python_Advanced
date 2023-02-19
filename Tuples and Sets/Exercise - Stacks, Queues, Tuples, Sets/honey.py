from collections import deque

bees = deque(int(x) for x in input().split())
nectars = deque(int(x) for x in input().split())
processes = deque(input().split())
functions = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}
honey = 0
while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()
    if nectar < bee:
        bees.appendleft(bee)
    elif nectar > bee:
        honey += abs(functions[processes.popleft()](bee, nectar))
print(f'Total honey made: {honey}')
if bees: print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectars: print(f'Nectar left: {", ".join(str(x) for x in nectars)}')
