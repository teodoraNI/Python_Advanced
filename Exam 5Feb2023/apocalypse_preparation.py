from collections import deque

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

products = {
    'Patch':30,
    'Bandage':40,
    'MedKit':100
}
created_items = {}

while medicaments and textiles:
    mix = textiles[0] + medicaments[-1]
    if mix in products.values():
        medicaments.pop()
        textiles.popleft()
        product = list(products.keys())[list(products.values()).index(mix)]
        if product not in created_items.keys():
            created_items[product] = 1
        else:
            created_items[product] += 1
    elif mix > products['MedKit']:
        if 'MedKit' not in created_items:
            created_items['MedKit'] = 1
        else:
            created_items['MedKit'] += 1
        remaining = medicaments.pop() + textiles.popleft() - products['MedKit']
        medicaments[-1] += remaining
    else:
        textiles.popleft()
        medicaments[-1] += 10

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")
elif not textiles:
    print("Textiles are empty.")
elif not medicaments:
    print("Medicaments are empty.")

if created_items:
    for item, quantity in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
        print(f"{item} - {quantity}")

if medicaments:
    print(f"Medicaments left: ", end = '')
    print(*(reversed(medicaments)),sep= ', ')
if textiles:
    print(f"Textiles left: ", end = '')
    print(*textiles, sep=', ')

