from collections import deque
M,N,H = map(int,input().split())

# M 가로, N 세로, H 높이
graph = []
for i in range(H):
    graph_h = []
    for j in range(N):
        graph_h.append(list(map(int,input().split())))
    graph.append(graph_h)

queue = deque()

for i in range(H):
    for j in range(N):
        for k in range(M):
            if graph[i][j][k] == 1:
                queue.append([i,j,k])

# 앞 뒤 왼쪽 오른쪽 위 아래
dx = [0,0,-1,1,0,0]
dy = [1,-1,0,0,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while queue:
        z,y,x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if (nx >= 0 and nx <M) and (ny >=0 and ny < N) and (nz >=0 and nz < H):
                if graph[nz][ny][nx] == 0:
                    graph[nz][ny][nx] = graph[z][y][x] + 1
                    queue.append([nz,ny,nx])

bfs()
day = 0
for i in range(H):
    for j in range(N):
        for k in range(M):
            day = max(day, graph[i][j][k] - 1)
            if graph[i][j][k] == 0:
                print(-1)
                quit()
print(day)