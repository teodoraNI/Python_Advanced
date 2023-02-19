from collections import deque
import sys

def best_list_pureness(*args):
    if len(args) == 2:
        nums_list, k = args[0], args[1]
        best_pureness = -sys.maxsize
        rotations = 0
        for i in range(k+1):
            my_list = deque(nums_list)
            pureness = 0
            my_list.rotate(i)
            for j in range(len(my_list)):
                if type(my_list[j]) == int:
                    pureness += my_list[j]*j
            if pureness > best_pureness:
                best_pureness = pureness
                rotations = i
    return f'Best pureness {best_pureness} after {rotations} rotations'

test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)