from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(input()))

queue = deque()
visited = [[False] * N for _ in range(N)]

dx = [0,0,-1,1]
dy = [1,-1,0,0]

count = 0
def bfs(i,j):
    queue.append([i,j])
    while queue:
        y,x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < N) and (0<= ny < N) and not visited[ny][nx] and graph[y][x]==graph[ny][nx]:
                visited[ny][nx] = True
                queue.append([ny,nx])
# 적록색약 아닐때
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            count+=1
print(count, end=" ")

# 적록색약일때
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * N for _ in range(N)]
count = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i,j)
            count+=1
print(count)


        
