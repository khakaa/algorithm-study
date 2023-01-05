import sys

input = sys.stdin.readline
w,n = map(int, input().split(' '))
jewels = [list(map(int, input().split(' '))) for _ in range(n)]
jewels.sort(key=lambda x : x[1], reverse=True)

total_price = 0
for j,p in jewels:
    if w > j:
        total_price += j*p
        w -= j
    else:
        total_price += w*p
        break

print(total_price)