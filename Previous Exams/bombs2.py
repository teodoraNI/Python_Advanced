from collections import deque

effects = deque(int(x) for x in input().split(', '))
casings = [int(x) for x in input().split(', ')]

bomb_types = {
    40:'Datura Bombs',
    60:'Cherry Bombs',
    120:'Smoke Decoy Bombs'
}
bombs = {'Datura Bombs':0, 'Cherry Bombs':0, 'Smoke Decoy Bombs':0}
success = False
while effects and casings:
    effect = effects.popleft()
    casing = casings.pop()
    if effect + casing in bomb_types.keys():
        bombs[bomb_types[effect+casing]] += 1
        if bombs['Datura Bombs'] >=3 and bombs['Cherry Bombs'] >= 3 and bombs['Smoke Decoy Bombs'] >=3:
            success = True
            break
    else:
        casings.append(casing - 5)
        effects.appendleft(effect)
print('Bene! You have successfully filled the bomb pouch!') if success else \
    print("You don't have enough materials to fill the bomb pouch.")
print("Bomb Effects: ", end='')

print(*effects, sep=', ') if effects else print('empty')
print("Bomb Casings: ", end='')
print(*casings, sep=', ') if casings else print('empty')
[print(f'{key}: {value}') for key, value in sorted(bombs.items())]
