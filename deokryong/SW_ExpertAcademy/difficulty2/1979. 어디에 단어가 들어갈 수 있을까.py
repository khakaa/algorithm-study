T = int(input())
for i in range(1,T+1):
    N, K = map(int,input().split())
    arr = []
    result = 0

    for j in range(N):
        arr.append([j for j in list(map(int,input().split()))])
    for j in range(N):
        count_row = 0
        count_col = 0
        for k in range(N):
            if arr[j][k] == 1:
                count_col += 1
                if k == N-1 and count_col == K:
                    result += 1
            if arr[k][j] == 1:
                count_row += 1
                if k == N-1 and count_row == K:
                    result += 1
            if arr[j][k] == 0:
                if count_col == K:
                    result+=1
                    count_col = 0
                else:
                    count_col = 0
            if arr[k][j] == 0:
                if count_row == K:
                    result+=1
                    count_row = 0
                else:
                    count_row = 0
                    
    print(f'#{i} {result}')