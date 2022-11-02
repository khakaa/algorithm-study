T = int(input())
for i in range(1,T+1):
    arr = input()
    arr_reverse = arr[-1::-1]
    result = 1
    if arr != arr_reverse:
        result = 0
    print(f'#{i} {result}')