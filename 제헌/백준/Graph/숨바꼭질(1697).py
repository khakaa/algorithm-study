from collections import deque

def bfs():
    queue = deque()
    queue.append(n)

    while queue:
        v = queue.popleft()
        if v == m:
            print(user_map[v])
            break
        
        for nx in (v-1, v+1, v*2):
            if 0 <= nx < 100001 and not user_map[nx]:
                user_map[nx] = user_map[v] + 1
                queue.append(nx)

n, m = map(int, input().split())

user_map = [0] * 100001

bfs()