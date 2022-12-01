N = int(input())

graph = []
INF = int(1e9)
# 그래프 초기화
for i in range(N):
    graph.append(list(input()))

# 그래프 재초기화 N->0, Y->1
for i in range(N):
    for j in range(N):
        if graph[i][j] == 'N':
            graph[i][j] = INF
        elif graph[i][j] == 'Y':
            graph[i][j] = 1

# 플로이드 워셜 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 자기 자신은 친구가 아니므로 0으로 초기화
for i in range(N):
    graph[i][i] = 0

# 그래프 확인
# for i in range(N):
#     for j in range(N):
#         print(graph[i][j],end=" ")
#     print()

# 가장 유명한 사람 찾기
max_friends = 0
for i in range(N):
    count = 0
    for j in range(N):
        if graph[i][j] != 0 and graph[i][j] <=2:
            count+=1
    if max_friends <= count:
        max_friends = count
    
print(max_friends)