import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

# 노드의 개수, 간선의 개수 입력받기
n, m = map(int,input().split())
# 시작 노드 번호 입력
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력받기
for _ in range(m):
    a,b,c=map(int,input().split())
    graph[a].append([b,c])

for i in range(n):
    print(graph[i])
def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        # 현재 탐색하는 노드가 기존 값보다 작을 경우 패스
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1,n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
    
# 도달할 수 없는 경우, 무한(INFINITY)로 출력
