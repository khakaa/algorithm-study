from collections import deque

n, k = map(int, input().split())

graph = [0] * (100001)
visited = [0] * (100001)
visited[n] = 1

def bfs():
    q = deque()
    q.append(n)

    while q:
        dx = q.popleft()

        if dx == k:
            print(graph[dx]) 

        for i in (dx*2, dx - 1, dx + 1):
            if dx*2 == i and 0 <= i <= 100000 and visited[i] == 0:
                q.append(i)
                graph[i] = graph[dx]
                visited[i] = 1

            if (i - 1 == dx or i + 1 == dx ) and 0 <= i <= 100000 and visited[i] == 0:
                q.append(i)
                graph[i] = graph[dx] + 1
                visited[i] = 1

bfs()