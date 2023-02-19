sequence = list(input())
open_parenthessis = []

for i in range(len(sequence)):
    if sequence[i] in '({[':
        open_parenthessis.append(sequence[i])
    elif not open_parenthessis:
        print('NO')
        exit()
    else:
        if f"{open_parenthessis.pop() + sequence[i]}" not in '(){}[]':
            print('NO')
            exit()
if not open_parenthessis:
    print('YES')
else:
    print('NO')


