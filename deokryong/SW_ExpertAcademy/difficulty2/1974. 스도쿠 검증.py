T = int(input())
for i in range(1,T+1):
    arr = []
    answer = 1
    for j in range(9):
        arr.append(list(map(int,input().split())))
    prefix_sum_arr = [[0]*10 for k in range(10)]
    for j in range(1,10):
        for k in range(1,10):
            prefix_sum_arr[j][k] = arr[j-1][k-1] + prefix_sum_arr[j][k-1] + prefix_sum_arr[j-1][k] - prefix_sum_arr[j-1][k-1]
    
    
    for j in range(9):
        x_sum = 0
        y_sum = 0
        for k in range(9):
            x_sum += arr[j][k]
            y_sum += arr[k][j]
        if x_sum != 45 or y_sum != 45:
            answer = 0
    
    x1,y1,x2,y2 = 0,0,2,2
    for j in range(3):
        for k in range(3):
            if prefix_sum_arr[y2+1][x2+1] - prefix_sum_arr[y1][x2+1] - prefix_sum_arr[y2+1][x1] + prefix_sum_arr[y1][x1] != 45:
                answer = 0
            x1+=3
            x2+=3
        y1+=3
        y2+=3
        x1 = 0
        x2 = 2
    print(f'#{i} {answer}')