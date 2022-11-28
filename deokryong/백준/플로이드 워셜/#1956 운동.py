N, M = map(int,input().split())

INF = int(1e9)
graph = [[INF]*(N+1) for _ in range(N+1)]

# 간선을 그래프에 추가
for i in range(M):
    a,b,c = map(int,input().split())
    graph[a][b] = c

# 자기 자신 0으로 초기화
for i in range(1,N+1):
    for j in range(1,N+1):
        if i==j:
            graph[i][j] = 0

# 플로이드 워셜 수행
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# 그래프를 탐색하면서 사이클을 형성하면 temp에 값 저장, answer을 통해 사이클 최소 값 저장
answer = -1
for i in range(1,N+1):
    temp = 0
    for j in range(1,N+1):
        if i != j and graph[i][j] != INF and graph[j][i] != INF:
            temp = graph[i][j] + graph[j][i]
            if answer == -1:
                answer = temp
            else:
                answer = min(answer,temp)
print(answer)