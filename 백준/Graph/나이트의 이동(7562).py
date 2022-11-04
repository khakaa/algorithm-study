from collections import deque

n = int(input())

for _ in range(n):
    board_len = int(input())
    graph = [[0] * (board_len) for _ in range(board_len)]

    cur_x, cur_y = map(int, input().split())
    tar_x, tar_y = map(int, input().split())
    cnt = 0

    dx, dy = [-1, -2, -2, -1, 1, 2, 2, 1], [2, 1, -1, -2, -2, -1, 1, 2]

    q = deque()
    q.append((cur_x, cur_y))
    
    while q:
        x, y = q.popleft()

        if x == tar_x and y == tar_y:
            print(graph[x][y])
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx <= board_len - 1 and 0 <= ny <= board_len - 1:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))