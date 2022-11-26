# n 도시 개수
# m 버스 개수
# a 버스 시작 도시, b 도착 도시, c 비용

n = int(input())
m = int(input())
INF = 1000000001
graph = [[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            graph[i][j] = 0

for i in range(m):
    a,b,c = map(int,input().split())
    if graph[a][b] > c:
        graph[a][b] = c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
print(graph)
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
        print(graph[i][j],end=" ")
    print()
