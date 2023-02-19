from collections import deque

green_light_secs = int(input())
free_window_secs = int(input())
cars = deque()
cars_passed = 0
while True:
    command = input()
    if command == 'END':
        break
    if command != 'green':
        cars.append(command)
    else:# when command is 'green'
        current_green_light_secs = green_light_secs
        while current_green_light_secs > 0 and cars:
            current_car = cars.popleft()
            if free_window_secs + current_green_light_secs < len(current_car):
                index_of_hit = current_green_light_secs + free_window_secs
                print(f'A crash happened!\n{current_car} was hit at {current_car[index_of_hit]}.')
                raise SystemExit
            current_green_light_secs -= len(current_car)
            cars_passed += 1
print(f"Everyone is safe.\n{cars_passed} total cars passed the crossroads.")

