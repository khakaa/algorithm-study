from collections import deque

def bfs(start):
    q = deque()
    q.append(start)
    graph[start] = 1
    
    while q:
        dx = q.popleft()
        
        if dx == k:
            ans[0] += 1
            
        for i in (dx - 1, dx + 1, 2 * dx):    
            if 0 <= i <= 100000 and (graph[i] == 0 or graph[i] >= graph[dx] + 1):
                graph[i] = graph[dx] + 1
                q.append(i)

n, k = map(int, input().split())
graph = [0 for _ in range(100001)]
ans = [0]

bfs(n)

print(graph[k] - 1)
print(ans[0])