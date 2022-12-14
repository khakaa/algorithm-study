import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

N,M,X = map(int,input().split())
graph = [[] for _ in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])

def dijkstra(start):
    distance = [INF] * (N+1)
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])
    return distance

total = [0]*(N+1)
for i in range(1,N+1):
    total[i]=(dijkstra(i)[X])

for i in range(1,N+1):
    total[i] += (dijkstra(X)[i])
    
print(max(total))