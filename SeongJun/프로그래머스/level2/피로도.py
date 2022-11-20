# 순열
# from itertools import permutations

# def solution(k, dungeons):
#     answer = 0
#     len_dungeons = len(dungeons)
#     for permu in permutations(dungeons, len_dungeons):
#         PRD = k
#         count = 0
#         for i in permu:
#             if PRD>=i[0]:
#                 PRD -=i[1]
#                 count +=1
#         if count > answer:
#             answer = count
#     return answer

# DFS
answer = 0
N = 0
visited = []


def dfs(k, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt

    for j in range(N):
        if k >= dungeons[j][0] and not visited[j]:
            visited[j] = 1
            dfs(k - dungeons[j][1], cnt + 1, dungeons)
            visited[j] = 0


def solution(k, dungeons):
    global N, visited
    N = len(dungeons)
    visited = [0] * N
    dfs(k, 0, dungeons)
    print(answer)
    return answer

if __name__ == "__main__":
    solution(80,[[80,20],[50,40],[30,10]])