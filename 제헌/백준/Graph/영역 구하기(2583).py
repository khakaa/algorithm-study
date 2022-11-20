from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * (n) for _ in range(m)]
visited = [[0] * (n) for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
cnt = 0
ans = []

for _ in range(k):
    a, b, c, d = map(int, input().split())

    for i in range(m - d, m - b):
        for j in range(a, c):
            if graph[i][j] == 1:
                continue
            else:
                graph[i][j] = 1

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    area = 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if visited[nx][ny] == 0 and graph[nx][ny] == 0:
                    area += 1
                    visited[nx][ny] = 1
                    q.append((nx, ny))

    return area

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0 and visited[i][j] == 0:
            cnt += 1
            ans.append(bfs(i, j))
ans.sort()

print(cnt)
print(*ans)