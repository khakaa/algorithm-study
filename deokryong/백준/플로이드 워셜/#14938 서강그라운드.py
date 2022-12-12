# 첫째줄 - n지역 개수, m수색범위, r길의 개수
# 두번째줄 - t각 지역에 있는 아이템의 수
# 세번째줄 - a지역 번호, b지역번호,ㅣ길의 길이

n, m, r = map(int,input().split())
items = list(map(int,input().split()))
INF = int(1e9)

# 그래프 초기화
graph = [[INF]*(n+1) for _ in range(n+1)]

# 양방향 간선 초기화
for i in range(r):
    a,b,l = map(int,input().split())
    graph[a][b] = l
    graph[b][a] = l

# 플로이드 워셜 수행
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

# 그래프 확인
for i in range(1,n+1):
    for j in range(1,n+1):
        print(graph[i][j],end=" ")
    print()

answer = []
for i in range(1,n+1):
    temp = items[i-1]
    for j in range(1,n+1):
        if i!=j:
            if graph[i][j] <= m:
                temp += items[j-1]
    answer.append(temp)
print(answer)