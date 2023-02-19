from collections import deque

boxes = [int(x) for x in input().split()]
magics = deque(int(x) for x in input().split())
presents = {}
functions = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle'
}
while boxes and magics:
    box = boxes.pop()
    magic = magics.popleft()
    magic_level = box * magic
    if magic_level in functions:
        if functions[magic_level] not in presents:
            presents[functions[magic_level]] = 0
        presents[functions[magic_level]] += 1
    elif magic_level < 0:
        boxes.append(box+magic)
    elif magic_level > 0:
        boxes.append(box + 15)
    elif magic_level == 0:
        if box == 0 and magic != 0:
            magics.appendleft(magic)
        elif magic == 0 and box != 0:
            boxes.append(box)
if {'Teddy bear', 'Bicycle'}.issubset(presents) or {"Doll", 'Wooden train'}.issubset(presents):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')
if boxes:
    print(f'Materials left: {", ".join(str(x) for x in reversed(boxes))}')
if magics:
    print(f'Magic left: {", ".join(str(x) for x in magics)}')
for key, value in sorted(presents.items()):
    print(f'{key}: {value}')





