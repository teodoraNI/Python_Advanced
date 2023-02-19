# from math import floor
# from collections import deque
#
# class Robot:
#     def __init__(self,name,processing_time):
#         self.name = name
#         self.processing_time = processing_time
#         self.busy_until = 0
#
#
# def get_seconds(time):
#     hour, min, sec = [int(x) for x in time.split(':')]
#     return hour*3600 + min*60 + sec
#
#
# def get_time(seconds):
#     seconds %= (24 * 60 * 60)
#     hour = seconds // (60 * 60)
#     min = floor((seconds / 60) % 60)
#     sec = seconds % 60
#     return f'{hour:02d}:{min:02d}:{sec:02d}'
#
# robots = []
# robots_data = input().split(';')
# for robot in robots_data:
#     name, processing_time = robot.split('-')
#     robots.append(Robot(name, int(processing_time)))
#
# time_in_secs = get_seconds(input())
# items = deque()
#
# while True:
#     item = input()
#     if item == 'End':
#         break
#     items.append(item)
# while items:
#     current_item = items.popleft()
#     time_in_secs += 1
#     found_robot = False
#     for robot in robots:
#         if time_in_secs >= robot.busy_until:
#             found_robot = True
#             robot.busy_until = time_in_secs + robot.processing_time
#             print(f'{robot.name} - {current_item} [{get_time(time_in_secs)}]')
#             break
#     if found_robot == False:
#         items.append(current_item)


from datetime import datetime, timedelta
from collections import deque

robots = {r.split('-')[0]: [int(r.split('-')[1]),0] for r in input().split(';')}
current_time = datetime.strptime(input(), '%H:%M:%S')
items = deque()
while True:
    item = input()
    if item == 'End':
        break
    items.append(item)
while items:
    current_item = items.popleft()
    current_time += timedelta(0, 1)
    robots = {r[0]: [r[1][0], r[1][1] - 1] if r[1][1] != 0 else r[1] for r in robots.items()}
    free_robots = list(filter(lambda x: x[1][1] == 0, robots.items()))
    if not free_robots:
        items.append(current_item)
        continue
    robots[free_robots[0][0]][1] = free_robots[0][1][0]
    print(f"{free_robots[0][0]} - {current_item} [{current_time.strftime('%H:%M:%S')}]")