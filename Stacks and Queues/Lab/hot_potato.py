from collections import deque

kids = deque(input().split())
number = int(input())

while len(kids) > 1:
    kids.rotate(-number)
    print(f'Removed {kids.pop()}')
print(f'Last is {kids.pop()}')
