k, n = map(int, input().split())
line_data = [int(input()) for _ in range(k)]
start, end = 1, max(line_data)

while start <= end:
    mid = (start + end) // 2
    lines = 0

    for line in line_data:
        lines += line // mid

    if lines >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)