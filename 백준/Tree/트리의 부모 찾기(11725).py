from collections import deque

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)
answer = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited[1] = 1

while q:
    v = q.popleft()

    for i in graph[v]:
        if not visited[i]:
            answer[i] = v
            q.append(i)
            visited[i] = 1

print(*answer[2:], sep='\n')