reservations = set()
guests = set()
for _ in range(int(input())):
    reservation = input()
    if len(reservation) == 8:
        reservations.add(reservation)
while True:
    info = input()
    if info == 'END':
        break
    guests.add(info)
result = sorted(reservations.difference(guests))
print(len(result))
print(*result, sep='\n')

