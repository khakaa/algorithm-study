from collections import deque

N,M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input())))

dxy = [[-1,0], [1,0], [0,-1], [0,1]] # 상하좌우

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    
    while queue:
        x,y = queue.popleft()
        # 상하좌우 이동
        for dx,dy in dxy:
            nx = dx + x
            ny = dy + y

            # 범위 넘어가면 넘어가기
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            # 0이면 넘어가기
            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx,ny))

bfs(0,0)
print(graph[N-1][M-1])