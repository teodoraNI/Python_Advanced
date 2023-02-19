jobs = [int(x) for x in input().split(', ')]
index_interest = int(input())
interest = jobs[index_interest]
time_needed = interest

for i in range(len(jobs)):
    if jobs[i] < interest and i != index_interest:
        time_needed += jobs[i]
    elif jobs[i] == interest and i < index_interest:
        time_needed += jobs[i]

print(time_needed)
