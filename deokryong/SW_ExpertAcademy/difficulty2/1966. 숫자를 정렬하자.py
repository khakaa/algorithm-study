T = int(input())
for i in range(1,T+1):
    N = int(input())
    arr = list(input().split())
    arr = sorted(arr,key=lambda x:(int(x)))
    print(f'#{i} {" ".join(arr)}')

