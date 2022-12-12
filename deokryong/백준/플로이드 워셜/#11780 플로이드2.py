n = int(input())
m = int(input())

INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
path = [[[]]*(n+1) for _ in range(n+1)]

for i in range(m):
    a,b,c = map(int,input().split())
    graph[a][b] = min(graph[a][b],c)

for i in range(1,n+1):
    for j in range(1,n+1):
        path[i][j] = [i,j]
        

#플로이드 워셜 수행
for k in range(1,n+1):
    graph[k][k] = 0
    path[k][k] = []
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                path[i][j] = path[i][k] + path[k][j][1:]

# 그래프 출력
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(0)
        elif graph[i][j] == INF:
            print(0)
        else:
            print(len(path[i][j])," ".join(map(str,path[i][j])))
    