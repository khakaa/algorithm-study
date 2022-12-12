N, M = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort(reverse=True)

temp = [0]*M

if N <= M:
    print(max(arr))
else:
    for i in range(M):
        temp[i] += arr.pop(0)
    while True:
        if len(arr) == 0:
            break    
        temp.sort()
        temp[0] += arr.pop(0)
    print(max(temp))