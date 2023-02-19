seq = [int(el) for el in input().split()]
pos = sum(n for n in seq if n>0)
neg = sum(n for n in seq if n<0)
print(neg)
print(pos)
if abs(neg) > pos:
    print('The negatives are stronger than the positives')
else:
    print('The positives are stronger than the negatives')