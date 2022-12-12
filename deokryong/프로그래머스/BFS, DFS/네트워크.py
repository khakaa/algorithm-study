# from collections import deque

# def solution(n, computers):
#     answer = 0
#     visited = [False] * n
        
#     def bfs(start):
#         q = deque()
#         q.append(start)
#         visited[start] = True
#         while q:
#             com = q.popleft()
#             for i in range(n):
#                 if computers[com][i] == 1 and visited[i] == False:
#                     visited[i] = True
#                     q.append(i)
#     for i in range(n):
#         if not visited[i]:
#             bfs(i)
#             answer += 1
#     return answer
def solution(n, computers):
    answer = 0
    visited = [False] * n
        
    def dfs(start):
        visited[start] = True
        for i in range(n):
            if computers[start][i] == 1 and visited[i] == False:
                dfs(i)
            
    for i in range(n):
        if not visited[i]:
            dfs(i)
            answer += 1
    print(answer)
    return answer
solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])
solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]])