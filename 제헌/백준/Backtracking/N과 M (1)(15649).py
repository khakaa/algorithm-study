def dfs():
    if len(user_data) == m:
        print(' '.join(user_data))
        return
    
    for i in range(1, n+1):
        if visited[i] == 0:
            visited[i] = 1
            user_data.append(str(i))
            dfs()
            user_data.pop()
            visited[i] = 0

n, m = map(int, input().split())
visited = [0] * (n + 1)
user_data = []

dfs()