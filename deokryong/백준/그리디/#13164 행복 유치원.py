import heapq
N, K = map(int,input().split())

arr = list(map(int,input().split()))
diff = []
for i in range(1,len(arr)):
    heapq.heappush(diff,-(arr[i]-arr[i-1]))


for i in range(K-1):
    heapq.heappop(diff)

print(-sum(diff))