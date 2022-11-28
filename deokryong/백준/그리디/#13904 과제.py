import heapq

N = int(input())

day_arr = [0] * 1001
heap_arr = []

for i in range(N):
    day, weight = map(int,input().split())
    heap_arr.append([-weight,day,weight])

heapq.heapify(heap_arr)

while True:
    if len(heap_arr) == 0:
        break
    temp = heapq.heappop(heap_arr)
    for j in range(temp[1],0,-1):
        if day_arr[j] == 0:
            day_arr[j] = temp[2]
            break
print(sum(day_arr))