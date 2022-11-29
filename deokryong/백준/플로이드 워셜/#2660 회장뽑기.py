N = int(input())
INF = int(1e9)

graph = [[INF]*(N+1) for _ in range(N+1)]

# 양방향 간선 초기화
while True:
    a,b = map(int,input().split())
    if a == -1 and b == -1:
        break
    graph[a][b] = 1
    graph[b][a] = 1

# 자기 자신 0 초기화
for i in range(1,N+1):
    graph[i][i] = 0

# 플로이드 워셜 수행
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 부연 설명 => graph[i][j] > graph[i][k] + graph[k][j] 일때 graph[i][j] = graph[i][k] + graph[k][j]로
# 초기화 시켜주는 이유 1. 친구사이 or 친구의 친구사이 or 친구의 친구의 친구사이 일경우 INF값 제거하기위함
# 2. 각 회원별 최대 값 구하기 위함

answer = []
president = 10000
for i in range(1,N+1):
    if president > max(graph[i][1:]):
        president = max(graph[i][1:])
for i in range(1,N+1):
    if president == max(graph[i][1:]):
        answer.append(i)
print(president,end=" ")
print(len(answer))
print(" ".join(map(str,answer)))