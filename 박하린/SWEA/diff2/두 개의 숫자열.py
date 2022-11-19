def get_ans(a,b,n,m):
    result = 0
    if n > m:
        for i in range(n - m + 1):
            c_sum = 0
            for j in range(m):
                c_sum += a[j+i] * b[j]
            result = max(result,c_sum)
    else:
        for i in range(m - n + 1):
            c_sum = 0
            for j in range(n):
                c_sum += b[j+i] * a[j]
            result = max(result,c_sum)
    return result

ans = []
t = int(input())
for _ in range(t):
    n,m = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    b = list(map(int, input().strip().split(' ')))
    ans.append(get_ans(a,b,n,m))

for i in range(len(ans)):
    print(f'#{i+1} {ans[i]}')