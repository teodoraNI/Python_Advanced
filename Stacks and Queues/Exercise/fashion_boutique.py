clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks = 1
current_capacity = rack_capacity
while clothes:
    if clothes[-1] <= current_capacity:
        current_capacity -= clothes.pop()
    else:
        current_capacity = rack_capacity
        racks += 1
print(racks)
