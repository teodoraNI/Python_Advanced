from collections import deque

portions = [int(x) for x in input().split(', ')]
staminas = deque([int(x) for x in input().split(', ')])
conquered_peaks = []

peaks = {
    'Vihren': 80, 'Kutelo': 90, 'Banski Suhodol': 100, 'Polezhan': 60, 'Kamenitza': 70}
while peaks and portions and staminas:
    if portions.pop() + staminas.popleft() < list(peaks.values())[0]:
        continue
    else:
        conquered_peaks.append(list(peaks.keys())[0])
        del peaks[list(peaks.keys())[0]]
if not peaks:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")
if conquered_peaks:
    print("Conquered peaks: ")
    print(*conquered_peaks, sep='\n')
