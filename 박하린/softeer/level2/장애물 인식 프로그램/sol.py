from collections import deque

n = int(input())
block = []
dxy = [[-1,0],[0,1],[1,0],[0,-1]]
for _ in range(n):
    block.append(list(map(int, list(input()))))

def dfs(i,j):
    cnt = 1
    queue = deque()
    queue.append((i,j))

    while queue:
        x,y = queue.popleft()

        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            elif block[nx][ny] == 1:
                block[nx][ny] = 'x'
                queue.append((nx,ny))
                cnt += 1
    return cnt

o_cnt = []
for i in range(n):
    for j in range(n):
        if block[i][j] == 1:
            block[i][j] = 'x'
            o_cnt.append(dfs(i,j))

o_cnt.sort()
print(len(o_cnt))
for i in range(len(o_cnt)):
    print(o_cnt[i])