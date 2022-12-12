from collections import deque

def bfs(start, graph, visited):
    q = deque()
    q.append(start)
    visited[start] = 1
    res = 1
    
    while q:
        x = q.popleft()
        
        for i in graph[x]:
            if not visited[i]:
                res += 1
                q.append(i)
                visited[i] = 1
                
    return res

def solution(n, wires):
    answer = int(1e9)
    graph = [[] for _ in range(n + 1)]
    
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    for a, b in wires:
        visited = [0] * (n + 1)
        visited[b] = 1
        res = bfs(a, graph, visited)
        
        if abs(res - (n - res)) < answer:
            answer = abs(res - (n - res))
            
    return answer