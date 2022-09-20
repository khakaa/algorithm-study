import sys
sys.setrecursionlimit(10000)

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    visited[x][y] = 1
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < h and 0 <= ny < w:
            if user_map[nx][ny] == 1 and not visited[nx][ny]:
                user_map[nx][ny] = 100
                dfs(nx, ny)

    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break

    user_map = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0] * w for _ in range(h)]
    cnt = 0

    for i in range(h):
        for j in range(w):
            if user_map[i][j] == 1 and visited[i][j] == 0:
                cnt += dfs(i, j)

    print(cnt)