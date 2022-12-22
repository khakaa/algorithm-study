import sys
import heapq

input = sys.stdin.readline
N, M = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
path = [INF] * (N+1)

def dijkstra(start):
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
                path[i[0]] = [now,i[0]]
                heapq.heappush(q,[cost,i[0]])
    count = 0
    
    for i in range(len(path)):
        if path[i] != INF:
            count += 1
    print(count)
    for i in range(len(path)):
        if path[i] == INF:
            continue
        print(f'{path[i][0]} {path[i][1]}')

for i in range(M):
    A,B,C = map(int,input().split())
    graph[A].append([B,C])
    graph[B].append([A,C])

dijkstra(1)
