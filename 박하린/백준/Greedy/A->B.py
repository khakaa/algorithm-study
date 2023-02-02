import sys
input = sys.stdin.readline

a,b = map(int, input().split())
cnt = 1

while a != b:
    temp = b

    if b % 2 == 0:
        b //= 2
        cnt += 1
    elif b % 10 == 1:
        b //= 10
        cnt += 1
    if temp == b:
        print(-1)
        break
else:
    print(cnt)