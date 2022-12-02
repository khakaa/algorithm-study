N = int(input())

graph = []
for i in range(N):
    graph.append(list(map(int,input().split())))

answer = [[1]*N for _ in range(N)]

result = 0
# 플로이드 워셜 수행
for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][j] != 0 and graph[i][k] != 0 and graph[k][j] != 0:
                if graph[i][j] == graph[i][k] + graph[k][j]:
                    answer[i][j] = 0
                elif graph[i][j] > graph[i][k] + graph[k][j]:
                    result = -1

if result != -1:
    for i in range(N):
        for j in range(N):
            if answer[i][j]:
                result += graph[i][j]
    print(result//2)
else:
    print(result)
