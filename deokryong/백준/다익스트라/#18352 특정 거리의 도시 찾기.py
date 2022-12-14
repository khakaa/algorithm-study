import sys
import heapq

#N 도시의 개수, M 도로의 개수, K 거리 정보, X 출발 도시
input = sys.stdin.readline
N, M, K, X = map(int,input().split())

INF = int(1e9)
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
for i in range(M):
    a,b = map(int,input().split())
    graph[a].append([b,1])

def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = i[1] + dist
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,[cost,i[0]])

    solution = []
    for i in range(len(distance)):
        if distance[i] == K:
            solution.append(i)
    return solution

answer = dijkstra(X)
answer.sort()
if len(answer) == 0:
    print(-1)
else:
    print("\n".join(map(str,answer)))