n = int(input())
matrix = list([x for x in list(input())] for i in range(n))
knights = [(i,j) for i in range(n) for j in range(n) if matrix[i][j] == 'K']
moves = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
counter = 0
while True:
    attacks = []
    max_attacks = 0
    for knight in knights:
        possible_attacks = set()
        for move in moves:
            possible_attacks.add((knight[0]+move[0], knight[1]+move[1]))
        attacks.append(len(possible_attacks.intersection(knights)))
        if len(possible_attacks.intersection(set(knights))) > max_attacks:
            max_attacks = len(possible_attacks.intersection(set(knights)))
            knight_to_be_removed = knight
    if sum(attacks) > 0:
        knights.remove(knight_to_be_removed)
        matrix[knight_to_be_removed[0]][knight_to_be_removed[1]] = '0'
        counter += 1
    else:
        break
print(counter)


