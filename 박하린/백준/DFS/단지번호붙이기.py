from collections import deque

N = int(input())
graph = []
dxy = [[-1,0], [0,1], [0, -1], [1,0]]

for _ in range(N):
    graph.append(list(map(int, input())))

def dfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0
    count = 1

    while queue:
        x,y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + ny

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            
            if graph[dx][dy] = 1:
                graph[dx][dy] = 0
                queue.append(dx,dy)
                count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            result.append(dfs(i,j))

result.sort()
print(len(result))
for r in result:
    print(r)