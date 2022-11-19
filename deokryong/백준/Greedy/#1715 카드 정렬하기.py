import heapq

N = int(input())
arr = []
for i in range(N):
    arr.append(int(input()))

heapq.heapify(arr)

answer = 0
temp = 0
    
while True:
    if len(arr)==1:
        break
    temp = heapq.heappop(arr) + heapq.heappop(arr)
    heapq.heappush(arr,temp)
    answer += temp
print(answer)
