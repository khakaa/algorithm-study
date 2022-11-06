T = int(input())

for i in range(1,T+1):
    N = int(input())
    result = 0
    for j in range(1,N+1):
        if j%2==0:
            result-=j
        else:
            result+=j
    print(f'#{i} {result}')