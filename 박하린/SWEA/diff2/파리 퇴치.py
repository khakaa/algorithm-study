t = int(input())
for t in range(t):
    n,m = map(int, input().split(' '))
    area = []
    for _ in range(n):
        area.append(list(map(int, input().strip().split(' '))))
    
    ans = 0

    # 0,1,2,3
    for i in range(n-m+1):
        # 0,1,2,3
        for j in range(n-m+1):
            cnt = 0

            for mi in range(m):
                for mj in range(m):
                    cnt += area[i+mi][j+mj]
            ans = max(ans,cnt)
    
    print(f'#{t+1} {ans}')
