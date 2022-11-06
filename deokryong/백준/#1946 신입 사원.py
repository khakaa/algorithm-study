# 1946

T = int(input())
for i in range(T):
    N = int(input())
    arr = [[0]*2 for _ in range(N)]
    people = 1
    for j in range(N):
        arr[j][0],arr[j][1] = map(int,input().split())
    arr.sort(key=lambda x : (x[0]))
    
    arr2 = [0]*N
    for j in range(N):
        arr2[j] = arr[j][1]
    last = arr2[0]

    for j in range(1,len(arr2)):
        if arr2[j] < last:
            last = arr2[j]
            people+=1
        
    print(people)
