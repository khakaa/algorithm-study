from collections import deque

N = int(input())
graph = []
dxy = [[-1,0], [0,1], [0,-1], [1,0]]

for _ in range(N):
    graph.append(list(map(int, input())))

def bfs(a,b):
    queue = deque()
    queue.append((a,b))
    graph[a][b] = 0 # 방문했다는 의미로 0으로 만들기
    count = 1 # 개수 1로 초기화

    while queue:
        x,y = queue.popleft()

        for nx,ny in dxy:
            dx = nx + x
            dy = ny + y

            if dx < 0 or dx >= N or dy < 0 or dy >= N:
                continue
            
            if graph[dx][dy] == 1:
                graph[dx][dy] = 0
                queue.append((dx,dy))
                count += 1
    return count

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1: # 그래프 값이 1이면 탐색 시작
            result.append(bfs(i,j))

result.sort()
print(len(result))
for r in result:
    print(r)