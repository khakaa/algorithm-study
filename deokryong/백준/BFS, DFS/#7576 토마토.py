from collections import deque

M, N = map(int,input().split())
# M은 가로, N은 세로
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            queue.append([i,j])

# 상하좌우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

visited = [[False] * M for _ in range(N)]

def bfs():
    while queue:
        y, x = queue.popleft()
        visited[y][x] = True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<M and 0<=ny<N and arr[ny][nx] == 0:
                if visited[ny][nx] == False:
                    arr[ny][nx] = arr[y][x] + 1
                    visited[ny][nx] = True
                    queue.append([ny,nx])
bfs()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            print()
print(arr)
