import heapq
N = int(input())

rooms = []
for i in range(N):
    start, end = map(int,input().split())
    heapq.heappush(rooms,[-end,start,end])

count = len(rooms)

print(rooms)
for i in range(len(rooms)-1):
    if rooms[i][1] >= rooms[i+1][2]:
        count -= 1 
print(count)