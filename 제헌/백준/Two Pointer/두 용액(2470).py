n = int(input())
user_data = list(map(int, input().split()))
user_data.sort()

start, end = 0, n - 1
answer = abs(user_data[start] + user_data[end])
res = [user_data[start], user_data[end]]

while start < end:
    start_val, end_val = user_data[start], user_data[end]
    cnt = start_val + end_val

    if abs(cnt) <= answer:
        answer = abs(cnt)
        res = [start_val, end_val]
        if answer == 0:
            break
    
    if cnt < 0:
        start += 1
    else:
        end -= 1

print(*res)