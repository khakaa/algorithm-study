from collections import deque
import copy
N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

dx = [0,0,-1,1]
dy = [1,-1,0,0]

answer = []

def find_safety(h):
    visited = [[False]*N for _ in range(N)]
    safety_graph = copy.deepcopy(graph)
    for i in range(N):
        for j in range(N):
            if safety_graph[i][j] > h and not visited[i][j]:
                safety_graph[i][j] = 1      # 잠기지 않은 지역
                visited[i][j] = True
            elif safety_graph[i][j] <= h and not visited[i][j]:
                safety_graph[i][j] = 0      # 잠긴 지역
                visited[i][j] = True
    return safety_graph


def bfs(y,x,g):
    q = deque()
    q.append([y,x])
    visited[y][x] = True
    while q:
        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < N and g[ny][nx] == 1 and not visited[ny][nx]:
                visited[ny][nx] = True
                q.append([ny,nx])


for i in range(101):
    temp = find_safety(i)
    visited = [[False]*N for _ in range(N)]
    count = 0
    for j in range(N):
        for k in range(N):
            if temp[j][k] == 1 and not visited[j][k]:
                bfs(j,k,temp)
                count += 1
  
    answer.append(count)
print(max(answer))