odds = set()
evens = set()

for i in range(int(input())):
    name = input()
    total = 0
    total = sum(ord(symbol) for symbol in name) // (i+1)
    if total % 2 == 0:
        evens.add(total)
    else:
        odds.add(total)
if sum(odds) == sum (evens):
    print(*odds.union(evens), sep=', ')
elif sum(odds) > sum(evens):
    print(*odds.difference(evens), sep=', ')
else:
    print(*odds.symmetric_difference(evens), sep=', ')

