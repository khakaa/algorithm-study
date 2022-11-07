from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
max_tmp = -100
answer = []

def bfs(start):
    visited = [0] * (n + 1)
    q = deque([start])
    visited[start] = 1
    cnt = 0

    while q:
        v = q.popleft()
        for i in graph[v]:
            if visited[i] == 0:
                visited[i] = 1
                q.append(i)
                cnt += 1
    
    return cnt

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)

for i in range(1, n + 1):
    res = bfs(i)
    if res > max_tmp:
        max_tmp = res
        answer = [i]
    elif res == max_tmp:
        answer.append(i)

print(*answer)