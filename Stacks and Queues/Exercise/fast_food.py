from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])
orders_left = False
print(max(orders))
while orders:
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()
    else:
        orders_left = True
        print('Orders left:', end = ' ')
        print(*orders)
        break
if not orders_left:
    print('Orders complete')