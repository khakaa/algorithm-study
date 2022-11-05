n, s = map(int, input().split())
user_data = list(map(int, input().split()))

start, end = 0, 0
ans = int(1e9)
res = 0

while True:
    if res >= s:
        ans = min(ans, end - start)
        res -= user_data[start]
        start += 1

    elif end == n:
        break

    else:
        res += user_data[end]
        end += 1

if ans == int(1e9):
    print(0)
else:
    print(ans)