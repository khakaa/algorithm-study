T = int(input())
for i in range(1,T+1):
    arr = input()
    result = 0
    temp = ''
    count = 0
    for j in range(len(arr)):
        temp += arr[j]
        count+=1
        if arr[len(temp):len(temp)*2] == temp:
            break
    print(f'#{i} {count}')

