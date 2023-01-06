from collections import deque
N = int(input())

graph = [[] for _ in range(N+1)]
parent = [0] * (N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if parent[i] == 0:
                q.append(i)
                parent[i] = v
bfs(1)
for i in range(len(parent[2:])):
    print(parent[i+2])

