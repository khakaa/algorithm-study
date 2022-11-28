N = int(input())
M = int(input())

graph = [[0] * (N+1) for _ in range(N+1)]

for i in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] == 1 or (graph[i][k] == 1 and graph[k][j] == 1):
                graph[i][j] = 1


for i in range(1,N+1):
    temp = graph[i].count(1)
    for j in range(1,N+1):
        if graph[j][i] == 1:
            temp+=1
    print(N-1-temp)
