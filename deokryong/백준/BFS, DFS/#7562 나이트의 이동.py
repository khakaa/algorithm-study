from collections import deque
import sys

input = sys.stdin.readline

T = int(input())

dx = [-2,-1,1,2,-2,-1,1,2]
dy = [1,2,2,1,-1,-2,-2,-1]

def bfs(x,y):
    graph[y][x] = 0
    q = deque()
    q.append([x,y])
    while q:
        x , y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < length and 0 <= ny < length and graph[ny][nx] == -1:
                graph[ny][nx] = graph[y][x] + 1
                q.append([nx,ny])
    return graph[goal[0]][goal[1]]

for i in range(T):
    answer = 0 
    length = int(input())
    current = list(map(int,input().split()))
    goal = list(map(int,input().split()))

    graph = [[-1]*length for _ in range(length)]
    answer = bfs(current[1],current[0])
    print(answer)