from collections import deque

N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input())))

visited = [[False] * N for _ in range(N)]

# 상, 하, 좌, 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

answer = []
def bfs(x,y):
    queue = deque()
    queue.append([x,y])
    visited[x][y] = True
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and visited[nx][ny] == False:
                visited[nx][ny] = True
                count += 1
                queue.append([nx,ny])
    return count

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and visited[i][j] == False:
            answer.append(bfs(i,j))
answer.sort()
print(len(answer))
for i in range(len(answer)):
    print(answer[i])