T = int(input())

for i in range(1,T+1):
    N, M = map(int,input().split())

    if N > M:
        arr_A = list(map(int,input().split()))
        arr_B = list(map(int,input().split()))
    else:
        arr_B = list(map(int,input().split()))
        arr_A = list(map(int,input().split()))

    max = -1
    for j in range(len(arr_A) - len(arr_B) + 1):
        temp = 0
        for k in range(len(arr_B)):
            temp += arr_B[k] * arr_A[j+k]
        if temp > max:
            max = temp
    print(f'#{i} {max}')
