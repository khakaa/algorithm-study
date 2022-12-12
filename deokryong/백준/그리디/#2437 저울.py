N = int(input())

arr = list(map(int,input().split()))

arr.sort()

temp = 0
for i in range(0,len(arr)):
    if temp+1 >= arr[i]:
        temp += arr[i]
    else:
        break

print(temp+1)