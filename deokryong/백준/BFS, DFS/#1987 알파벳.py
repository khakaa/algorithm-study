import copy
R,C = map(int,input().split())

graph = []
max_count = [[1] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
for i in range(R):
    graph.append(list(input()))

chk_Alpha = []
            
# 상 하 좌 우
dx = [0,0,-1,1]
dy = [1,-1,0,0]

def dfs(y,x,chk_Alpha,visited):
    chk_Alpha_copy = copy.deepcopy(chk_Alpha)
    chk_Alpha_copy.append(graph[y][x])
    visited_copy = copy.deepcopy(visited)
    visited_copy[y][x] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < C and 0 <= ny < R and not visited_copy[ny][nx] and graph[ny][nx] not in chk_Alpha_copy:
            max_count[ny][nx] = max_count[y][x] + 1
            dfs(ny,nx,chk_Alpha_copy,visited_copy)

dfs(0,0,chk_Alpha,visited)
print(max(map(max,max_count))) 