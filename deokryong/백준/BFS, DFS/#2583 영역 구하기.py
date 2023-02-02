from collections import deque
import sys
input = sys.stdin.readline

M,N,K = map(int,input().split())

graph = []
for i in range(M):
    graph.append([0] * N)

visited = [[False] * N for _ in range(M)]
answer = []

for i in range(K):
    x1,y1,x2,y2 = map(int,input().split())
    for j in range(M-y2,M-y1):
        for k in range(x1,x2):
            graph[j][k] = 1

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(t1,t2):
    count = 0
    q = deque()
    q.append([t1,t2])
    visited[t1][t2] = True
    while q:
        y,x = q.popleft()
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and graph[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([ny,nx])
    if count != 0:
        answer.append(count)
for i in range(M):
    for j in range(N):
        if graph[i][j] == 0 and not visited[i][j]:
            bfs(i,j)
answer.sort()      

print(len(answer))
print(" ".join(map(str,answer)))