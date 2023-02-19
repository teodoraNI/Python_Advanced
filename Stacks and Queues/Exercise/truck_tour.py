from collections import deque

petrol_pumps_number = int(input())
pumps_data = deque([[int(x) for x in input().split()] for _ in range(petrol_pumps_number)])
start_index = 0
fuel = 0
start_index_found = False
while not start_index_found:
    for i in range(petrol_pumps_number):
        fuel += pumps_data[i][0]
        if fuel >= pumps_data[i][1]:
            fuel -= pumps_data[i][1]
            if i == petrol_pumps_number - 1:
                start_index_found = True
        else:
            pumps_data.rotate(-1)
            start_index += 1
            fuel = 0
            break
print(start_index)


