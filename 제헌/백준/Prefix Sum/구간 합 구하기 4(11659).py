import sys
input = sys.stdin.readline

n, m = map(int, input().split())
user_data = list(map(int, input().split()))
res_arr = [0]
res = 0

for i in range(n):
    res += user_data[i]
    res_arr.append(res)

for _ in range(m):
    a, b = map(int, input().split())
    print(res_arr[b] - res_arr[a - 1])