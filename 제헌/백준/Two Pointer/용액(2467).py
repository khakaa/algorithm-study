n = int(input())
data = list(map(int, input().split()))
start, end = 0, n - 1
res = 2147483647 * 2
ans1, ans2 = 0, 0

while start < end:
    if abs(data[start] + data[end]) < res:
        ans1, ans2 = data[start], data[end]
        res = abs(data[start] + data[end])

    if data[start] + data[end] < 0:
        start += 1

    else:
        end -= 1

print(ans1, ans2)