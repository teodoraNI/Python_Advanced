from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = [int(x) for x in input().split()]
locks = deque([int(x) for x in input().split()])
reward = int(input())
cost = 0
bullets_counter = 0
while bullets and locks:
    bullets_counter += 1
    cost += bullet_price
    if bullets.pop() <= locks[0]:
        print('Bang!')
        locks.popleft()
    else:
        print('Ping!')
    if bullets_counter == gun_barrel_size and bullets:
        print('Reloading!')
        bullets_counter = 0
if not locks:
    print(f'{len(bullets)} bullets left. Earned ${reward - cost}')
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

