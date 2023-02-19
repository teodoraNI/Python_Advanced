from collections import deque

customers = deque([int(x) for x in input().split(', ')])
taxis = [int(x) for x in input().split(', ')]

total_time = 0
while customers and taxis:
    if customers[0] <= taxis[-1]:
        total_time += customers.popleft()
        taxis.pop()
    else:
        taxis.pop()
if not customers:
    print(f'All customers were driven to their destinations\nTotal time: {total_time} minutes')
elif not taxis:
    print('Not all customers were driven to their destinations\nCustomers left:', end = ' ')
    print(*customers, sep=', ')



