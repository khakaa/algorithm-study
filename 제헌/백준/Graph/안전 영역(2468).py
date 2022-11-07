from collections import deque

n = int(input())

user_map = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, h):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if user_map[nx][ny] > h and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1

area_cnt = 0

for i in range(min(map(min, user_map)) - 1, max(map(max, user_map))):
    visited = [[0] * n for _ in range(n)]
    cnt = 0

    for j in range(n):
        for k in range(n):
            if user_map[j][k] > i and visited[j][k] == 0:
                bfs(j, k, i)
                cnt += 1
    if cnt > area_cnt:
        area_cnt = cnt

print(area_cnt)