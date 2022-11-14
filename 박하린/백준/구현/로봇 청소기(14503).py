# 북, 동, 하, 서
dx = [-1,0,1,0] 
dy = [0,1,0,-1]

n, m = map(int, input().split(' '))
r, c, d = map(int, input().split(' '))
area = []
visited = [[0 for _ in range(n)] for _ in range(m)]

for _ in range(n):
    area.append(list(map(int, input().split(' '))))

visited[r][c] = 1
cnt = 1

while 1:
    flag = 0
    for _ in range(4):
        d = (d+3) % 4 # 왼쪽 방향으로 회전
        nx = r + dx[d]
        ny = c + dy[d]

        # 범위 안에 들고 청소 가능
        if 0 <= nx < n and 0 <= ny < m and area[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                flag = 1 # 청소
                break
    
    # 네 방향 모두 청소 되있거나 벽임
    if flag == 0:
        # 후진했을 때 벽
        if area[r-dx[d]][c-dy[d]] == 1:
        