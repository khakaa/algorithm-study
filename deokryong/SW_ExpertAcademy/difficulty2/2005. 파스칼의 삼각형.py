T = int(input())

for i in range(1,T+1):
    N = int(input())
    arr = [1]
    temp = 2
    for j in range(2,N+1):
        if j == 2:
            arr.append(1)
            arr.append(1)
        else:
            for k in range(1,j+1):
                if k==1:
                    arr.append(arr[len(arr)-temp])
                elif k == j:
                    arr.append(arr[len(arr)-temp])
                else:
                    arr.append(arr[len(arr)-temp-1]+arr[len(arr)-temp])
            temp+=1
    print(f'#{i}')
    count = 0
    temp = 0
    for j in range(len(arr)):
        if temp == count:
            print(arr[j],end=" ")
            print()
            count=0
            temp+=1
        else:
            print(arr[j],end=" ")
            count+=1
