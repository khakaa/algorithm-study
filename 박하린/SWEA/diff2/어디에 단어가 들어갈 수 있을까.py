# 3 6 9
# 2 5 8
# 1 4 7

# 1 (0,0) (2,0) 이전 행 -> 회전 열, n-1-이전 열 -> 회전 행
# 2 (0,1) (1,0)
# 3 (0,2) (0,0)

# 오른쪽 90도 회전
def rotate_90(N,puzzle):
    ret = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            ret[N-1-j][i] = puzzle[i][j]
    return ret

# 1인거 카운트
def count_one_area(puzzle,N,K):
    result = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0 or j == N-1:
                if cnt == K:
                    result += 1
                cnt = 0
                
    return result

ans = []
t = int(input())
for _ in range(t):
    N,K = map(int, input().strip().split(' '))
    puzzle = []
    for _ in range(N):
        puzzle.append(list(map(int,input().strip().split(' '))))

    ret_puzzle = rotate_90(N,puzzle)
    ans.append(count_one_area(puzzle,N,K) + count_one_area(ret_puzzle,N,K))


for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')
    

