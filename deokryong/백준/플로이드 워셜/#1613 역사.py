n,k = map(int,input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(k):
    a,b = map(int,input().split())
    graph[a][b] = -1
    graph[b][a] = 1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k] == -1 and graph[k][j] == -1:
                graph[i][j] = -1
                graph[j][i] = 1

for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end=" ")
    print()

s = int(input())
for i in range(s):
    a,b = map(int,input().split())    
    print(graph[a][b])
