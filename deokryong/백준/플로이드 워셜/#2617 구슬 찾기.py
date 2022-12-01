N,M = map(int,input().split())

# 그래프 초기화
graph = [[0]*(N+1) for _ in range(N+1)]
for i in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1

# 플로이드 워셜 수행
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

count = 0
for i in range(1,N+1):
    chk_col = graph[i][1:].count(1)
    chk_row = 0
    for j in range(1,N+1):
        if graph[j][i] == 1:
            chk_row += 1
    if chk_col > N//2:
        count+=1
    if chk_row > N//2:
        count+=1

print(count)