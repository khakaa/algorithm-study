n = int(input())
k = int(input())
graph = [[] * n for _ in range(n + 1)]
visited = [0] * (n+1)

def dfs(start):
    visited[start] = 1
    for i in graph[start]:
        if visited[i] == 0:
            dfs(i)

for _ in range(k):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(sum(visited) - 1)
print(visited)