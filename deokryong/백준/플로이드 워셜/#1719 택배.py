n, m = map(int,input().split())

INF = int(1e9)
# 그래프 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]
answer = [[INF]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b, c = map(int,input().split())
    graph[a][b] = c
    graph[b][a] = c
    answer[a][b] = b
    answer[b][a] = a

# 플로이드 워셜 수행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]
                # 중간노드를 경유하는 경로의 첫 노드를 저장(*핵심 코드)
                answer[i][j] = answer[i][k]
                
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == j:
            print('-',end=" ")
        else:
            print(answer[i][j],end=" ")
    print()