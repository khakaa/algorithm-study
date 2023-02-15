import sys

input = sys.stdin.readline

n = int(input())
line = [list(map(int, input().rstrip().split())) for _ in range(n-1)]
a_n, b_n = map(int, input().rstrip().split())

a_time = 0
b_time = 0

a_i = 0
b_i = 0

for i in range(n-1):
    if n == 1:
        break

    a_time = min(a_i + line[i][0], line[i][1] + line[i][3] + b_i) # a에서만 작업, b 작업 + b에서 이동 + a 작업 중 작은 것
    b_time = min(b_i + line[i][1], line[i][0] + line[i][2] + a_i)

    a_i = a_time
    b_i = b_time

a_i += a_n
b_i += b_n

print(min(a_i,b_i))