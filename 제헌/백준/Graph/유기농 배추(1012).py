from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and farm_map[nx][ny] == 1:
                farm_map[nx][ny] = 0
                queue.append((nx, ny))
    return 1

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    farm_map = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):
        row_idx, col_idx = map(int, input().split())
        farm_map[col_idx][row_idx] = 1

    for i in range(n):
        for j in range(m):
            if farm_map[i][j] == 1:
                cnt += bfs(i, j)
    print(cnt)