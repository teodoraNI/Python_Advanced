from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milks = deque([int(x) for x in input().split(', ')])
milkshakes = 0
while milkshakes < 5 and chocolates and milks:
    chocolate = chocolates.pop()
    milk = milks.popleft()
    if milk <= 0 and chocolate <= 0:
        continue
    elif milk <= 0:
        chocolates.append(chocolate)
        continue
    elif chocolate <= 0:
        milks.appendleft(milk)
        continue

    if chocolate == milk:
        milkshakes += 1
    else:
        milk.append(milk)
        chocolates.append(chocolate-5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print('Not enough milkshakes.')
print(f'Chocolate: {", ".join(str(x) for x in chocolates) or "empty"}')
print(f'Milk: {", ".join(str(x) for x in milks) or "empty"}')
