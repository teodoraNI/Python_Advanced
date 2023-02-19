def fill_the_box(*args):
    box_volume = args[0]*args[1]* args[2]
    for arg in args[3:-1]:
        if arg != 'Finish':
            box_volume -= arg
        else:
            break
    if box_volume>0:
        return f'There is free space in the box. You could put {box_volume} more cubes.'
    return f'No more free space! You have {abs(box_volume)} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5,"Finish"))