from collections import deque

cups = deque([int(x) for x in input().split()])
bottles = [int(x) for x in input().split()]
wasted_water = 0
while cups and bottles:
    if bottles[-1] >= cups[0]:
        wasted_water += bottles.pop() - cups.popleft()
    else:
        cups[0] -= bottles.pop()
if cups:
    print(f'Cups:', end = ' ')
    [print(x, end=' ') for x in cups]
else:
    print(f'Bottles:', end = ' ')
    [print(x, end=' ') for x in bottles]
print(f'\nWasted litters of water: {wasted_water}')





