T = int(input())
for i in range(1,T+1):
    N,M = map(int,input().split())
    arr = []
    prefix_sum_arr = [[0]*(N+1) for z in range(N+1)]
    for j in range(N):
        arr.append(list(map(int,input().split())))
    for j in range(1,N+1):
        for k in range(1,N+1):
            prefix_sum_arr[j][k] = arr[j-1][k-1] + prefix_sum_arr[j-1][k] + prefix_sum_arr[j][k-1] - prefix_sum_arr[j-1][k-1]
 
    max = -1
    temp = 0
    x1,y1,x2,y2 = 0,0,M-1,M-1
    for j in range(N-M+1):
        for k in range(N-M+1):
            temp = prefix_sum_arr[y2+1][x2+1] - prefix_sum_arr[y1][x2+1] - prefix_sum_arr[y2+1][x1] + prefix_sum_arr[y1][x1]
            if max < temp:
                max = temp
            x1+=1
            x2+=1
        x1=0
        x2=M-1
        y1+=1
        y2+=1
    print(f'#{i} {max}')

