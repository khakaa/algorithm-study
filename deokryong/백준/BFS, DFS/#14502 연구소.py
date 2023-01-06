import sys
import copy
input = sys.stdin.readline

N, M = map(int,input().split())
graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

max_security = 0

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def select_wall(start,count):
    global max_security
    if count == 3:
        temp_graph = copy.deepcopy(graph)
        for r in range(N):
            for c in range(M):
                spread_virus(r,c,temp_graph)
        temp_max_security = sum(i.count(0) for i in temp_graph)
        max_security = max(temp_max_security,max_security)
    else: 
         for i in range(start, N*M): # 2차원 배열에서 조합 구하기
            r = i // M
            c = i % M
            if graph[r][c] == 0 : # 안전영역인 경우 벽으로 선택가능
                graph[r][c] = 1 # 벽으로 변경
                select_wall(i,count+1) # 벽선택
                print(i,count+1)
                graph[r][c] = 0


def spread_virus(y,x,graph):
    if graph[y][x] == 2:
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            if nx < M and nx >= 0 and ny >= 0 and ny < N:
                if graph[ny][nx] == 0:
                    graph[ny][nx] = 2
                    spread_virus(ny,nx,graph)

select_wall(0,0)
print(max_security)
