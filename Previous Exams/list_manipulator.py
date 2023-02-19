
def list_manipulator(nums_list, *args):
    action, place, *some = args
    if action == 'add' and place == 'beginning':
        nums_list = some + nums_list
    elif action == 'add' and place == 'end':
        nums_list.extend(some)
    elif action == 'remove' and place == 'beginning':
        if some == []:
            nums_list.pop(0)
        elif len(some) == 1 and some[0] <= len(nums_list):
            for i in range(some[0]):
                nums_list.pop(0)
    elif action == 'remove' and place == 'end':
        if some == []:
            nums_list.pop()
        elif len(some) == 1 and some[0] <= len(nums_list):
            for i in range(some[0]):
                nums_list.pop()

    return nums_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
