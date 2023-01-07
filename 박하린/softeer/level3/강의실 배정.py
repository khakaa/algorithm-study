import sys,heapq
input = sys.stdin.readline

heap = []
cnt = 0
n = int(input().rstrip())

for _ in range(n):
    s,e = map(int, input().rstrip().split())
    heapq.heappush(heap, (e,s))

end_time=0
while heap:
    if heap[0][1] >= end_time:
        end_time = heapq.heappop(heap)[0]
        cnt += 1
    else:
        heapq.heappop(heap)

print(cnt)
