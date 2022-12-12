import heapq
N = int(input())

arr_start_end = []
rooms = []

for i in range(N):
    start, end = map(int,input().split())
    arr_start_end.append([start,end])

arr_start_end.sort()

heapq.heappush(rooms,arr_start_end[0][1])

for i in range(1,len(arr_start_end)):
    if arr_start_end[i][0] < rooms[0]:
        heapq.heappush(rooms,arr_start_end[i][1])
    else:
        heapq.heappop(rooms)
        heapq.heappush(rooms,arr_start_end[i][1])

print(len(rooms))
