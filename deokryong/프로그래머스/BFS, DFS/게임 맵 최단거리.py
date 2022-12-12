from collections import deque
def solution(maps):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    answer = 0
    
    def bfs():
        q = deque()
        q.append([0,0])
        while q:
            y, x = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= len(maps[0]) or ny < 0 or ny >= len(maps):
                    continue
                if maps[ny][nx] == 1:
                    q.append([ny,nx])
                    maps[ny][nx] = maps[y][x] + 1
        return maps[len(maps)-1][len(maps[0])-1] if maps[len(maps)-1][len(maps[0])-1] > 1 else -1
    answer = bfs()
    return answer
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]])
solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]])
