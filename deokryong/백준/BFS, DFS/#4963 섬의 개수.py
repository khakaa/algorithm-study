# w 너비 h 높이
# 1 땅 0 바다
from collections import deque

# 상 하 좌 우 왼쪽위 오른쪽위 왼쪽아래 오른쪽아래
dx = [0,0,-1,1,-1,1,-1,1]
dy = [1,-1,0,0,1,1,-1,-1]

def bfs(y,x):
    queue.append([y,x])
    visited[y][x] = True
    while queue:
        y,x = queue.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<w and 0<=ny<h and not visited[ny][nx] and graph[ny][nx]==1:
                visited[ny][nx] = True
                queue.append([ny,nx])
while True:
    w,h = map(int,input().split())
    if w == 0 and h == 0:
        break
    graph = []
    for i in range(h):
        graph.append(list(map(int,input().split())))
    
    queue = deque()
    visited = [[False]*w for _ in range(h)]
    count = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and not visited[i][j]:
                bfs(i,j)
                count+=1
    print(visited)
    print(count)