import sys
input = sys.stdin.readline
n = int(input())
target1, target2 = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]        # 노드 저장할 graph 리스트 초기화
visited = [False] * (n+1)               # 방문 여부 판별할 visited 리스트 초기화
for i in range(m):                      # graph에 노드 저장
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)
answer = 1                              
chk = False                             # 촌수 있는지 없는지 판별하기 위한 변수
def dfs(start,ans):                     
    global answer
    global chk 
    if chk == True:                     # 촌수 확인 되면 dfs 종료
        return
    visited[start] = True               
    for i in graph[start]:              
        if i == target2:                
            chk = True
            answer = ans
        if not visited[i]:              
            dfs(i,ans+1)

dfs(target1,answer)
if chk == False:
    answer = -1

print(answer)

import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
target1, target2 = map(int,input().split())
m = int(input())

graph = [[] for _ in range(n+1)]        # 노드 저장할 graph 리스트 초기화
visited = [0] * (n+1)                   # 방문 여부 판별 + 몇촌인지 저장할 visited 리스트 초기화
for i in range(m):                      # graph에 노드 저장
    x,y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(start):                     
    q = deque()
    q.append(start)
    while q:
        v = q.popleft()
        for i in graph[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)
bfs(target1)
if visited[target2] == 0:   # visited[target2] == 0이면 촌수를 계산할 수 없는 경우이므로 -1출력
    print(-1)
else:                                   
    print(visited[target2])
