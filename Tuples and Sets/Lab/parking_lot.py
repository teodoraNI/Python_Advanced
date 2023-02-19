cars_in_parking = set()
map_function = {
    'IN': lambda x: cars_in_parking.add(x),
    'OUT': lambda x: cars_in_parking.discard(x)
}
for _ in range(int(input())):
    direction, number = input().split(', ')
    map_function[direction](number)
if cars_in_parking:
    print(*cars_in_parking, sep='\n')
else:
    print('Parking Lot is Empty')

